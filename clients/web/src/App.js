import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Feed from './Feed'

const API_URL = 'http://localhost:8080'


function App() {
  const [data, setData] = useState({ items: [] })
  useEffect(() => {
    async function fetchData() {
      // You can await here
      const response = await fetch(API_URL + '/feed/otters').then((resp) => resp.json).then((data) => {
        const { feed } = data;
        return feed;
      })
      setData(response);
    }
    fetchData();
  }, []); // Or [] if effect doesn't need props or state
  
  return (
    <div className="App">
      <header className="App-header">
        <p>The Wall App</p>
      </header>
      <Feed/>
    </div>
  );
}

export default App;
