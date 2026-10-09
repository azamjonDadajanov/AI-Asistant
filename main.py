import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

app = FastAPI(title="Gemini API FastAPI Example", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

ai_client = genai.Client(api_key=API_KEY)

class ChatMessage(BaseModel):
    role: str = Field(..., description="The role of the message sender, either 'user' or 'model'.")
    content: str = Field(..., description="The content of the message.")

class ChatRequest(BaseModel):
    history: List[ChatMessage] = Field(..., description="The chat history as a list of messages.")
    message: str = Field(..., description="The new message to send to the chat model.")
    system_introductins: Optional[str] = Field(None, description="System instructions for the chat model.")

class ChatResponse(BaseModel):
    reply: str = Field(..., description="The reply from the chat model.")
    status: str = Field(..., description="The status of the chat request.")

@app.get("/")
async def root():
    return {"message": "Welcome to the Gemini API FastAPI Example"}

@app.post('/api/chat', response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_endpoint(chat_request: ChatRequest):
    try:
        formatted_messages = []
        if chat_request.history:
            for msg in chat_request.history:
                formatted_messages.append(types.Content(role='user' if msg.role.lower() == 'user' else 'model', parts=[{'text': msg.content}]))
        formatted_messages.append(types.Content(role='user', parts=[{'text': chat_request.message}]))
        config = types.GenerateContentConfig(
            temperature=0.7,
            system_instruction=chat_request.system_introductins if chat_request.system_introductins else "You are a helpful assistant. for python coding!"
        )
        response = await ai_client.aio.models.generate_content(model="gemini-3.5-flash",config=config, contents=formatted_messages)

        if not response.text:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No response from the chat model.")

        return ChatResponse(reply=response.text, status="success")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)