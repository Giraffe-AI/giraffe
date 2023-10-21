import React, { useState } from 'react';
import giraffe from '../assets/giraffe.png';
import './Header.css';

function Header() {

  return (
    <div className='header'>
      <div className='left'>
        <p>giraffe.study</p>
      </div>
      <div className='right'>
        <button onClick={() => console.log('About Us clicked')}>about us</button>
        <button onClick={() => console.log('Contacts clicked')}>contacts</button>
      </div>
    </div>
  )
}

export default Header