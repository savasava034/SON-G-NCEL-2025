import React, { useState, useEffect } from 'react';
import './ModuleStatus.css';

function ModuleStatus() {
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchModuleStatus();
  }, []);

  const fetchModuleStatus = async () => {
    try {
      const response = await fetch('/api/modules');
      const data = await response.json();
      if (data.status === 'success') {
        setModules(data.modules);
      }
    } catch (error) {
      console.error('Error fetching module status:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="module-status loading">Loading modules...</div>;
  }

  return (
    <div className="module-status">
      <h3>Available Modules</h3>
      <div className="module-grid">
        {modules.map((module, index) => (
          <div key={index} className={`module-card ${module.status}`}>
            <div className="module-name">{module.name}</div>
            <div className="module-description">{module.description}</div>
            <div className={`module-badge ${module.status}`}>
              {module.status}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ModuleStatus;
