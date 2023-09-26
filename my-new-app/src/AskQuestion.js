import React, { useState } from 'react';
import axios from 'axios';

const AskQuestion = () => {
  const [question, setQuestion] = useState('');
  const [verse, setVerse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5000/ask', { question });
      setVerse(response.data.relevant_verse);
    } catch (error) {
      console.error('There was an error asking the question:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask your question"
        />
        <button type="submit">Ask</button>
      </form>
      {verse && (
        <div>
          <h2>Most Relevant Verse:</h2>
          <p>{verse}</p>
        </div>
      )}
    </div>
  );
};

export default AskQuestion;

