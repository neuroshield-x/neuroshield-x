import React, { useEffect, useState } from 'react';
import './App.css';
import LogList from './components/LogList';

function App() {
  const [alert, setAlert] = useState(null);

  useEffect(() => {
    const fetchAlert = () => {
      fetch('http://127.0.0.1:8000/api/detect')
        .then(res => res.json())
        .then(data => setAlert(data))
        .catch(err => console.error(err));
    };

    fetchAlert(); // initial call
    const interval = setInterval(fetchAlert, 10000);
    return () => clearInterval(interval); // cleanup
  }, []);

  return (
    <div className="app-container">
      <h1 className="title">🛡️ NeuroShield X</h1>
      <h4 className="subtitle">AI-Powered Threat Detection</h4>

      {alert && (
        <div className="alert-card">
          <div className="alert-header">🚨 Alert: {alert.event}</div>
          <div className="alert-body">
            <p><strong>Time:</strong> {alert.timestamp}</p>
            <p><strong>Source IP:</strong> {alert.ip}</p>
            <p><strong>Anomaly Score:</strong> {alert.anomalyScore}</p>
            <p className="explanation"><strong>Explanation:</strong> {alert.explanation}</p>
            <p className="recommendation"><strong>Recommendation:</strong> {alert.recommendation}</p>
          </div>
        </div>
      )}

      <hr />
      <LogList />
    </div>
  );
}

export default App;
