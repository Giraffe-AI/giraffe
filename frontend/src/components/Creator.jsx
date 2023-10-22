import React, { forwardRef, useState } from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeCreators from '../assets/giraffe-creators.png';
import './Generator-Generic.css';

const Creator = forwardRef((props, ref) => {

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
                        onChange={(event) => setTopic(event.target.value)}
                    />
                    <div className='dropdown-container'>
                        <div className='pre-form'>
                            <img src={notepad} alt='notepad' />
                            <span>What do you need help with?</span>
                        </div>
                        <select className='dropdown' onChange={handleParam1Change}>
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
                        <select className='dropdown' onChange={handleParam2Change}>
                            <option value='short'>{'< 1 min'}</option>
                            <option value='med'>1-2 minutes</option>
                            <option value='long'>{'> 2 mins'}</option>
                        </select>
                    </div>
                    <button className="submit-button" onClick={(event) => props.postRequest(event, requestData)}>create your video</button>
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
});

export default Creator