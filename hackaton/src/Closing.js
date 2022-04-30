import React from 'react'
import "./Closing.css"

export default function Closing() {
  return (
    <div className="Closing">
      <div className='score-section'>
        <p>Better luck next time</p>
        <p className='score-display'>SCORE: <span className='score'></span> 0 </p>
      </div>
      <div className="buttons">
          <button className='share'>SHARE</button>
          <button className='reset'>PLAY AGAIN!</button>
      </div> 
    </div>
  )
}