import React, { useRef, event } from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import Learner from './components/Learner';
import Creator from './components/Creator';
import Researcher from './components/Researcher';
import './App.css';

export default function App() {

  const learnerRef = useRef(null);
  const creatorRef = useRef(null);
  const researcherRef = useRef(null);

  const handleClick = () => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  };

  function postRequest(event, requestData) {
    event.preventDefault();
    fetch('http://localhost:3001/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <Header handleClick={handleClick} />
      <Welcome learnerRef={learnerRef} creatorRef={creatorRef} researcherRef={researcherRef} />
      <Learner ref={learnerRef} postRequest={postRequest} />
      <Creator ref={creatorRef} postRequest={postRequest} />
      <Researcher ref={researcherRef} postRequest={postRequest} />
    </div>
  )
};
