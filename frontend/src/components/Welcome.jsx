import React from 'react';
import './Welcome.css';
import giraffe from '../assets/giraffe.png';

const Welcome = ({ learnerRef, creatorRef, researcherRef }) => {

  const learnerClick = (e) => {
    e.preventDefault();
    learnerRef.current.scrollIntoView({ behavior: "smooth" });
  };

  const creatorClick = (e) => {
    e.preventDefault();
    creatorRef.current.scrollIntoView({ behavior: "smooth" });
  };

  const researcherClick = (e) => {
    e.preventDefault();
    researcherRef.current.scrollIntoView({ behavior: "smooth" });
  };

  const everyoneClick = () => {
    window.location.href = '/video';
  };

  return (
    <div>
      <div className='pre-heading'>
        <p>
          Unlock your learning potential
          <br />
          with tailored video explanations
        </p>
      </div>
      <div className='heading'>
        <h1>
          giraffe.st&nbsp;&nbsp;&nbsp;dy
        </h1>
      </div>
      <div className='main'>
        <div className='left'>
          <ul>
            <li onClick={learnerClick}>For learners</li>
            <li onClick={creatorClick}>For creators</li>
            <li onClick={researcherClick}>For researchers</li>
            <li onClick={everyoneClick}>For <eo>everyone!</eo></li>
          </ul>
        </div>
        <div className='right'>
          <img src={giraffe} alt='giraffe' />
        </div>
      </div>
      <div className='post-main'>
        <p>
          Get personalized video content that explains
          <br />
          complex topics in the way you'll understand best
        </p>
      </div>
    </div>
  )
}

export default Welcome