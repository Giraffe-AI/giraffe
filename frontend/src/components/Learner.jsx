import React from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeLearners from '../assets/giraffe-learners.png';
import './Generator-Generic.css';

function Learner() {

    return (
        <div>
            <div className='generator-header'>
                <h1>For learners</h1>
                <p>
                Select your topic and tell us your level of expertise. 
                We'll generate a video explanation 
                <br />
                curated just for you. 
                Whether you're an expert or a beginner, we've got you covered.
                </p>
            </div>
            <div className='generator-container'>
                <div className='user-form'>
                    <input
                        type='text'
                        className='input-oval'
                        placeholder='What are diods and how do they work?'
                    />
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={notepad} alt='notepad' />
                            <span>How detailed should the explanation be?</span>
                        </div>
                        <select className='dropdown'>
                            <option value='general'>General Terms</option>
                            <option value='overview'>Expert Overview</option>
                            <option value='indepth'>In-Depth Explanation</option>
                        </select>
                    </div>
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={clock} alt='clock' />
                            <span>How much time do you want to spend learning?</span>
                        </div>
                        <select className='dropdown'>
                            <option value='general'>As little as possible</option>
                            <option value='overview'>A fair bit</option>
                            <option value='indepth'>I want to know everything</option>
                        </select>
                    </div>
                </div>
                <div className='giraffe-container'>
                    <img
                        src={giraffeLearners}
                        alt='giraffe learners'
                        className='giraffe'
                    />
                </div>
            </div>
        </div>
    )
}

export default Learner