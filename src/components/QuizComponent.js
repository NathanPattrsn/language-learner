import React, { useState } from 'react';

const questions = [
  {
    question: "How do you say 'Hello' in Spanish?",
    options: ['Hola', 'Bonjour', 'Hallo', 'Ciao'],
    answer: 'Hola',
  },
  {
    question: "How do you say 'Thank you' in French?",
    options: ['Gracias', 'Danke', 'Merci', 'Grazie'],
    answer: 'Merci',
  },
];

function QuizComponent() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  const handleAnswerOptionClick = (selectedOption) => {
    if (selectedOption === questions[currentQuestion].answer) {
      setScore(score + 1);
    }

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
    }
  };

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Language Quiz</h2>
        {showScore ? (
          <div>
            <p className="card-text">You scored {score} out of {questions.length}</p>
          </div>
        ) : (
          <div>
            <p className="card-text">{questions[currentQuestion].question}</p>
            {questions[currentQuestion].options.map((option, index) => (
              <button key={index} className="btn btn-secondary mr-2" onClick={() => handleAnswerOptionClick(option)}>
                {option}
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default QuizComponent;
