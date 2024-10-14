import React, { useState } from 'react';

function DashboardComponent() {
  const [progress] = useState({
    lessonsCompleted: 5,
    quizzesTaken: 3,
    speakingPractice: 20, // minutes
  });

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">User Progress</h2>
        <p className="card-text">Lessons Completed: {progress.lessonsCompleted}</p>
        <p className="card-text">Quizzes Taken: {progress.quizzesTaken}</p>
        <p className="card-text">Speaking Practice: {progress.speakingPractice} minutes</p>
      </div>
    </div>
  );
}

export default DashboardComponent;
