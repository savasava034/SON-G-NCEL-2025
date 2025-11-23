import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import Results from './components/Results';
import Header from './components/Header';
import ModuleStatus from './components/ModuleStatus';
import './App.css';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    // Check API health on mount
    fetch('/api/health')
      .then(res => res.json())
      .then(data => {
        setApiStatus('connected');
      })
      .catch(err => {
        setApiStatus('disconnected');
        console.error('API connection error:', err);
      });
  }, []);

  const handleSearch = async (query, searchType) => {
    setLoading(true);
    try {
      const response = await fetch('/api/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query, type: searchType }),
      });
      
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Search error:', error);
      setResults({ status: 'error', message: error.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header apiStatus={apiStatus} />
      <div className="container">
        <div className="main-content">
          <h1 className="title">ARISTO</h1>
          <p className="subtitle">Quran Research & Discovery System</p>
          
          <SearchBar onSearch={handleSearch} loading={loading} />
          
          {loading && (
            <div className="loading">
              <div className="spinner"></div>
              <p>Searching and analyzing...</p>
            </div>
          )}
          
          {results && !loading && <Results data={results} />}
          
          <ModuleStatus />
        </div>
      </div>
    </div>
  );
}

export default App;
