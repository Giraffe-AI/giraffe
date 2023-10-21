import React from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeResearchers from '../assets/giraffe-researchers.png';
import './Generator-Generic.css';

function Researcher() {

    return (
        <div className='generator'>
            <div className='generator-header'>
                <h1>For researchers</h1>
                <p>
                Submit the link to a research paper and receive a quick video explanation.
                <br />
                Share the essence of your work with the world in a way that everyone can understand.
                </p>
            </div>
            <div className='generator-container'>
                <div className='user-form'>
                    <input
                        type='text'
                        className='input-oval'
                        placeholder='Submit your link here'
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
                    <button className="submit-button">explain your paper</button>
                </div>
                <div className='giraffe-container'>
                    <img
                        src={giraffeResearchers}
                        alt='giraffe researchers'
                        className='giraffe-researchers'
                    />
                </div>
            </div>
        </div>
    )
}

export default Researcher