import React from 'react';
import './App.css';
import AskQuestion from './AskQuestion';  // Make sure the path is correct

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Quran Interpretor</h1>
      </header>
      <main className="main-content">
        <AskQuestion />
      </main>
    </div>
  );
}

export default App;
