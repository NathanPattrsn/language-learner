import React from 'react';
import DashboardComponent from './components/DashboardComponent';
import LessonComponent from './components/LessonComponent';
import SpeechRecognitionComponent from './components/SpeechRecognitionComponent';
import ChatbotComponent from './components/ChatbotComponent';
import QuizComponent from './components/QuizComponent';

function App() {
  return (
    <div className="container mt-4">
      <h1 className="text-center">AI-Powered Language Learning Platform</h1>
      <DashboardComponent />
      <LessonComponent />
      <SpeechRecognitionComponent />
      <ChatbotComponent />
      <QuizComponent />
    </div>
  );
}

export default App;
