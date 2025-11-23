import React from 'react';
import './Results.css';

function Results({ data }) {
  if (!data) return null;

  if (data.status === 'error') {
    return (
      <div className="results error">
        <h3>Error</h3>
        <p>{data.message}</p>
      </div>
    );
  }

  return (
    <div className="results">
      <div className="results-header">
        <h2>Search Results</h2>
        <span className="results-count">
          {data.total || 0} results found
        </span>
      </div>

      {data.results && data.results.length > 0 ? (
        <div className="results-list">
          {data.results.map((result, index) => (
            <div key={index} className="result-item">
              <div className="result-header">
                <span className="verse-id">{result.verse_id}</span>
                <span className="result-score">{result.score}%</span>
              </div>
              <div className="result-content">
                <p className="arabic">{result.text_arabic || 'N/A'}</p>
                <p className="translation">{result.translation || 'N/A'}</p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="no-results">
          <p>No results found. Try a different search query.</p>
        </div>
      )}
    </div>
  );
}

export default Results;
