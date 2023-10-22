import React, { forwardRef, useState } from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeLearners from '../assets/giraffe-learners.png';
import './Generator-Generic.css';

const Learner = forwardRef((props, ref) => {

    const [topic, setTopic] = useState('');
    const [param1, setParam1] = useState('general');
    const [param2, setParam2] = useState('general');

    let requestData = {
        Type: "Creator",
        Topic: topic,
        Param1: param1,
        Param2: param2
    };

    function handleParam1Change(event) {
        setParam1(event.target.value);
    }

    function handleParam2Change(event) {
        setParam2(event.target.value);
    }

    return (
        <div className='generator' ref={ref}>
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
                        onChange={(event) => setTopic(event.target.value)}
                    />
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={notepad} alt='notepad' />
                            <span>How detailed should the explanation be?</span>
                        </div>
                        <select className='dropdown' onChange={handleParam1Change}>
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
                        <select className='dropdown' onChange={handleParam2Change}>
                            <option value='general'>As little as possible</option>
                            <option value='overview'>A fair bit</option>
                            <option value='indepth'>I want to know everything</option>
                        </select>
                    </div>
                    <button className="submit-button" onClick={(event) => props.postRequest(event, requestData)}>start learning now</button>
                </div>
                <div className='giraffe-container'>
                    <img
                        src={giraffeLearners}
                        alt='giraffe learners'
                        className='giraffe-learners'
                    />
                </div>
            </div>
        </div>
    )
});

export default Learner