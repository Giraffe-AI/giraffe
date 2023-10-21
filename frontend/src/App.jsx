import React, { useRef } from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import Learner from './components/Learner';
import Creator from './components/Creator';
import Researcher from './components/Researcher';
import './App.css';

function App() {

  const learnerRef = useRef(null);
  const creatorRef = useRef(null);
  const researcherRef = useRef(null);

  return (
    <div>
      <Header />
      <Welcome learnerRef={learnerRef} creatorRef={creatorRef} researcherRef={researcherRef} />
      <Learner ref={learnerRef} />
      <Creator ref={creatorRef}/>
      <Researcher ref={researcherRef}/>
    </div>
  )
}

export default App
