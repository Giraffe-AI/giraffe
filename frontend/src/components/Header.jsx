import React, { useState } from 'react';
import './Header.css';

function Header() {

  const handleClick = () => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  };

  return (
    <div className='header'>
      <div className='left'>
        <p onClick={handleClick}>giraffe.study</p>
      </div>
      <div className='right'>
        <button onClick={() => console.log('About Us clicked')}>about us</button>
        <button onClick={() => console.log('Contacts clicked')}>contacts</button>
      </div>
    </div>
  )
}

export default Header