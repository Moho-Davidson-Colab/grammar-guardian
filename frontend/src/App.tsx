import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Auth } from './pages/Auth';
import { Home } from './pages/Home';
import React from 'react';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <Auth/ >} />
        <Route path="/home" element={<Home/ >} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
