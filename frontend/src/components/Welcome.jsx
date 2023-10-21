import React, { useState } from 'react';
import './Welcome.css';
import giraffe from '../assets/giraffe.png';

function Welcome() {
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
            <li href='#learner'>For learners</li>
            <li>For creators</li>
            <li>For researchers</li>
            <li>For <eo>everyone!</eo></li>
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