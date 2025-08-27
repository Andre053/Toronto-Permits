import React, {useState} from 'react';
import './App.css';
import TorontoMap from './components/TorontoMap';
import NavBar from './components/NavBar'
import 'leaflet/dist/leaflet.css'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
//import BrowserRouter

// make these into separate components
function About() {
    return <h1>About page</h1>
}

function Stats() {
    return <h1>Stats page</h1>
}


function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <NavBar/>
        <Routes>
          <Route path="/" element={<TorontoMap/>}/>
          <Route path="/home" element={<TorontoMap/>}/>
          <Route path="/about" element={<About/>}/>
          <Route path="/map" element={<TorontoMap/>}/>
          <Route path="/stats" element={<Stats/>}/>
        </Routes>

      </div>
    </BrowserRouter>
    
  );
}

export default App;
