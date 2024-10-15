import React, { useState } from 'react';

function ChatbotComponent() {
  const [userInput, setUserInput] = useState('');
  const [chatLog, setChatLog] = useState([]);

  const handleUserInput = async (e) => {
    e.preventDefault();
    const response = await fetch('https://language-learner-vyfk.onrender.com//api/chatbot', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();
    
    // Access the reply correctly
    setChatLog([...chatLog, { user: userInput, bot: data.response }]);
    setUserInput('');
  };

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Chat with the AI Bot</h2>
        <div>
          {chatLog.map((chat, index) => (
            <div key={index}>
              <strong>You:</strong> {chat.user}<br />
              <strong>Bot:</strong> {chat.bot}<br />
            </div>
          ))}
        </div>
        <form onSubmit={handleUserInput}>
          <input 
            type="text" 
            value={userInput} 
            onChange={(e) => setUserInput(e.target.value)} 
            placeholder="Type a message..." 
            className="form-control" 
          />
          <button type="submit" className="btn btn-primary mt-2">Send</button>
        </form>
      </div>
    </div>
  );
}

export default ChatbotComponent;
