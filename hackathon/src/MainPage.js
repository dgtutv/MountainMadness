import React from 'react'
import "./MainPage.css"

export default function Opening() {
  return (
    <div className="MainPage">
        <p className='picture'> PICTURE WILL GO HERE </p>
        <div className='choises'>
            <button className='btn'> Option 1 </button>
            <button className='btn'> Option 2 </button>
            <button className='btn'> Option 3 </button>
            <button className='btn'> Option 4 </button>
        </div>
    </div>
  )
}