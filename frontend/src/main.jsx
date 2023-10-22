import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import App from './App.jsx'
import Video from './Video.jsx'
import tempVideo from "./assets/giraffe_gif.mp4";
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route index={true} path="/home" element={<App />} />
      <Route index={true} path="/video/load" element={<Video video={tempVideo}/>} />
      <Route index={true} path="/video/result" element={<Video video='final'/>} />
    </Routes>
  </BrowserRouter>
)
