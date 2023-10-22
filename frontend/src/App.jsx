import React, { useState, useRef, useEffect } from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import Learner from './components/Learner';
import Creator from './components/Creator';
import Researcher from './components/Researcher';
import './App.css';

export default function App() {

  const [videoStatus, setVideoStatus] = useState('');

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

  useEffect(() => {
    // fetches video status from the server
    const fetchVideoStatus = () => {
      fetch('http://localhost:3001/video-status')
        .then(response => response.json())
        .then(data => {
          setVideoStatus(data.video);
        })
        .catch((error) => {
          console.error('Error fetching video status:', error);
        });
    };

    // call fetchVideoStatus now to do an initial fetch
    fetchVideoStatus();

    // sets up polling every 1 second
    const interval = setInterval(() => {
      fetchVideoStatus();
    }, 1000); // 10000 milliseconds = 10 seconds

    // cleans up the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  // redirects to '/video' if videoStatus is 'temp'
  useEffect(() => {
    if (videoStatus === 'temp') {
      window.location.href = '/video/load';
    } else if (videoStatus && videoStatus !== 'temp') {
      window.location.href = '/video/result';
    }
  }, [videoStatus]); // runs whenever videoStatus changes

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
