import React from 'react'
import "./Opening.css"
import MainPage from './MainPage';

function startTheGame(){
  return
}

export default function Opening() {
  return (
    <div className="Opening">
        <button className='start-button' onClick={startTheGame}> START </button>
    </div>
  )
}

