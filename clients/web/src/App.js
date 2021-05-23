import React, { useState } from 'react';
import './App.css';
import Feed from './components/Feed';
import Search from './components/Search';

function App() {
  const [query, setQuery] = useState("");

  return (
    <div className="App">
      <header className="App-header">
        <p>The Wall App</p>
      </header>
      <Search query={query} setQuery={setQuery} style={{width: "50%"}}/>
      <div style={{width: "85%", margin: "auto"}}>
        <Feed query={query} />
      </div>
    </div>
  );
}

export default App;
