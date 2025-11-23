import React from 'react';
import './Header.css';

function Header({ apiStatus }) {
  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">ARISTO</div>
        <div className="nav">
          <span className={`status-indicator ${apiStatus}`}>
            {apiStatus === 'connected' ? '● Connected' : '● Disconnected'}
          </span>
        </div>
      </div>
    </header>
  );
}

export default Header;
