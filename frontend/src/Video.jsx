import React from 'react';
import Header from './components/Header';
import './Video.css';
import './components/Generator-Generic.css';
import clock from './assets/clock.png';
import notepad from './assets/notepad.png';

export default function Video({ video }) {

    const handleClick = () => {
        window.location.href = '/home';
    };

    return (
        <div>
            <Header handleClick={handleClick} />
            <div className='video-page'>
                <input
                    type='text'
                    className='input-oval'
                    placeholder='Would you like to change anything?'
                />
                <br />
                <div className='video-mid'>
                    <div className='video-container'>
                        <video width="600" height="400" controls >
                            <source src={video} type="video/mp4" />
                        </video>
                    </div>
                    <div>
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
                        <button className="submit-button">create your video</button>
                    </div>
                </div>
            </div>
        </div>
    )
};