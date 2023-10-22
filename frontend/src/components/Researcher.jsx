import React, { forwardRef } from 'react';
import clock from '../assets/clock.png';
import notepad from '../assets/notepad.png';
import giraffeResearchers from '../assets/giraffe-researchers.png';
import './Generator-Generic.css';

const Researcher = forwardRef((props, ref) => {

    const handleSubmit = (event) => {
        event.preventDefault();
        const fileInput = document.getElementById('file-input');
        const file = fileInput.files[0];
        if (!file) {
            alert('Please choose a file to submit.');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        // Send formData to server using fetch or axios
    };

    return (
        <div className='generator' ref={ref}>
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
                    <form onSubmit={handleSubmit}>
                        <div className='file-input'>
                            <label htmlFor="file-input" className="custom-file-upload">
                                Upload a PDF:
                            </label>
                            <input id="file-input" type="file" />
                        </div>
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
                        <button className="submit-button" type="submit">Submit file</button>
                    </form>
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
});

export default Researcher