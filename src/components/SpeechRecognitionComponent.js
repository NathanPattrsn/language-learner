import React, { useState } from 'react';

function SpeechRecognitionComponent() {
  const [transcript, setTranscript] = useState('');
  const [feedback, setFeedback] = useState('');

  const startListening = () => {
    const recognition = new window.SpeechRecognition();
    recognition.lang = 'en-US'; // Change to your target language
    recognition.start();

    recognition.onresult = (event) => {
      const currentTranscript = event.results[0][0].transcript;
      setTranscript(currentTranscript);
      analyzePronunciation(currentTranscript);
    };
  };

  const analyzePronunciation = async (text) => {
    const response = await fetch('https://language-learner-vyfk.onrender.com/api/analyze-pronunciation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    setFeedback(data.feedback); // Display feedback to the user
  };
  

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Practice Speaking</h2>
        <button className="btn btn-primary" onClick={startListening}>Start Speaking</button>
        <p className="mt-2">Transcript: {transcript}</p>
        <p className="mt-2">Feedback: {feedback}</p>
      </div>
    </div>
  );
}

export default SpeechRecognitionComponent;
