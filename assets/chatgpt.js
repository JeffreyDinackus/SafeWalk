const apiKey = 'YOUR_API_KEY'; // Replace with your ChatGPT API key
const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions'; // API endpoint

const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
  const userMessage = userInput.value;
  if (userMessage.trim() !== '') {
    appendMessage('You', userMessage);

    // Send user message to ChatGPT API
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt: userMessage,
        max_tokens: 50, // Adjust this as needed
      }),
    })
      .then(response => response.json())
      .then(data => {
        const chatGPTResponse = data.choices[0].text;
        appendMessage('ChatGPT', chatGPTResponse);
      })
      .catch(error => console.error(error));

    userInput.value = ''; // Clear user input
  }
});

function appendMessage(sender, message) {
  const messageDiv = document.createElement('div');
  messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatLog.appendChild(messageDiv);
}


