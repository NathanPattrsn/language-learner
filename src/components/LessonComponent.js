import React, { useState, useEffect } from 'react';

function LessonComponent() {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    const fetchLessons = async () => {
      const response = await fetch('https://language-learner-vyfk.onrender.com//api/recommended-lessons'); // Correct URL
      const data = await response.json();
      setLessons(data);
    };    
    fetchLessons();
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Personalized Language Lessons</h2>
        <ul className="list-group">
          {lessons.map((lesson) => (
            <li key={lesson.id} className="list-group-item">{lesson.title}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default LessonComponent;
