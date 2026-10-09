const API_URL = 'http://127.0.0.1:8000/api/chat';

const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const typingIndicator = document.getElementById('typing-indicator');
const clearBtn = document.getElementById('clear-btn');

const systemIntroductins = "Sen python dasturchisisan"

let chatHistory = [];

function appendMessage(role, content) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', role);
    const bubleDiv = document.createElement('div');
    bubleDiv.classList.add('bubble');
    bubleDiv.textContent = content;
    messageElement.appendChild(bubleDiv);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const userMessage = userInput.value;
    if (!userMessage.trim()) return;
    appendMessage('user', userMessage);
    userInput.value = '';
    typingIndicator.classList.remove('hidden');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage, history: chatHistory, role: 'user', system_introductins: systemIntroductins })
        });
        
        if(response.statusText === 'OK') {
            const data = await response.json();
            typingIndicator.classList.add('hidden');
            appendMessage('model', data.reply);
            chatHistory.push({ role: 'user', content: userMessage });
            chatHistory.push({ role: 'model', content: data.reply });
        } else{
            typingIndicator.classList.add('hidden');
            console.error('Error:', response.statusText);
            appendMessage('model', 'Error: Unable to get response from the server.');
        }
    } catch (error) {
        typingIndicator.classList.add('hidden');
        console.error('Error:', error);
    }
});

clearBtn.addEventListener('click', () => {
    chatBox.innerHTML = '';
    chatHistory = [];
});