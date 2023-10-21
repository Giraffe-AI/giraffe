import React from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeCreators from '../assets/giraffe-creators.png';
import './Generator-Generic.css';

function Creator() {

    return (
        <div className='generator'>
            <div className='generator-header'>
                <h1>For creators</h1>
                <p>
                Speed up your educational video creation with our 3Blue1Brown style generator. 
                <br />
                Enhance your audience's learning experience with high-quality, customized content.
                </p>
            </div>
            <div className='generator-container'>
                <div className='user-form'>
                    <input
                        type='text'
                        className='input-oval'
                        placeholder='What are your thoughts about the project?'
                    />
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={notepad} alt='notepad' />
                            <span>What do you need help with?</span>
                        </div>
                        <select className='dropdown'>
                            <option value='brainstorm'>Brainstorming</option>
                            <option value='content'>Generating content</option>
                            <option value='edit'>Editing</option>
                        </select>
                    </div>
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={clock} alt='clock' />
                            <span>How long do you want your video to be?</span>
                        </div>
                        <select className='dropdown'>
                            <option value='short'>{'< 1 min'}</option>
                            <option value='med'>1-2 minutes</option>
                            <option value='long'>{'> 2 mins'}</option>
                        </select>
                    </div>
                    <button className="submit-button">create your video</button>
                </div>
                <div className='giraffe-container'>
                    <img
                        src={giraffeCreators}
                        alt='giraffe creators'
                        className='giraffe-creators'
                    />
                </div>
            </div>
        </div>
    )
}

export default Creator