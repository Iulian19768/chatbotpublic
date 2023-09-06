// chatbot-widget.js

// JavaScript code for your chatbot widget
const chatbotWidget = document.createElement('div');
chatbotWidget.id = 'chatbot-widget';
chatbotWidget.innerHTML = '<img id="open-chat-btn" src="message_app/images/ICo3_resized.png" alt="Chatbot Icon" />';

// Attach the chatbot widget to the document body
document.body.appendChild(chatbotWidget);

// Function to open the chatbot
function openChatbot() {
    const chatbox = document.getElementById('chatbox');
    chatbox.classList.toggle('open'); // Toggle the chatbox visibility
}

// Event listener to open the chatbot when the widget is clicked
chatbotWidget.addEventListener('click', openChatbot);
