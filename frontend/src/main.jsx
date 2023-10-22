import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import App from './App.jsx'
import Video from './Video.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route index={true} path="/home" element={<App />} />
      <Route index={true} path="/video" element={<Video />} />
    </Routes>
  </BrowserRouter>
)
