const chat = document.getElementById('chat');
const input = document.getElementById('message');
const sendBtn = document.getElementById('send');

function addMessage(text, sender) {
  const msg = document.createElement('div');
  msg.className = `message ${sender}`;
  msg.textContent = text || "";
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
  return msg;
}

function showTyping() {
  const typing = document.createElement('div');
  typing.className = 'typing bot';
  typing.id = 'typing-indicator';
  typing.textContent = 'Escribiendo...';
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;
}

function removeTyping() {
  const typingMsg = document.getElementById('typing-indicator');
  if (typingMsg) chat.removeChild(typingMsg);
}

async function sendMessage() {
  const pregunta = input.value.trim();
  if (!pregunta) return;

  addMessage(pregunta, 'user');
  input.value = '';
  showTyping();

  try {
    const response = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ pregunta })
    });

    removeTyping();

    if (!response.ok || !response.body) {
      addMessage('Error al obtener la respuesta del bot.', 'bot');
      return;
    }

    // Creamos un mensaje vacío para ir escribiendo
    const msg = addMessage('', 'bot');

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      msg.textContent += decoder.decode(value, { stream: true });
      chat.scrollTop = chat.scrollHeight;
    }
  } catch (error) {
    removeTyping();
    addMessage('Hubo un problema de conexión.', 'bot');
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});
