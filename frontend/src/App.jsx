import React from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import Learner from './components/Learner';
import Creator from './components/Creator';
import Researcher from './components/Researcher';
import './App.css';

function App() {

  return (
    <div>
      <Header />
      <Welcome />
      <Learner />
      <Creator />
      <Researcher />
    </div>
  )
}

export default App
