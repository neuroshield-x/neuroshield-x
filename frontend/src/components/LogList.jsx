import React, { useEffect, useState } from 'react';

const LogList = () => {
  const [logs, setLogs] = useState([]);
  const [lastUpdated, setLastUpdated] = useState(null);

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/logs');
        const data = await res.json();
        setLogs(data.reverse()); // latest first
        setLastUpdated(new Date().toLocaleTimeString());
      } catch (err) {
        console.error('Failed to fetch logs', err);
      }
    };

    fetchLogs();
    const interval = setInterval(fetchLogs, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>📋 Live Logs</h2>
      <p style={{ fontSize: '0.9rem', color: '#888' }}>
        Last updated: {lastUpdated || 'Loading...'}
      </p>

      {logs.length === 0 ? (
        <p style={{ color: '#ccc' }}>No logs available.</p>
      ) : (
        <table border="1" cellPadding="10" style={{ width: '100%', fontFamily: 'monospace' }}>
          <thead>
            <tr>
              <th>Time</th>
              <th>IP</th>
              <th>Event</th>
              <th>Score</th>
              <th>Explanation</th>
              <th>Recommendation</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, index) => (
              <tr key={index}>
                <td>{log.timestamp}</td>
                <td>{log.ip}</td>
                <td>{log.event}</td>
                <td>{log.anomalyScore}</td>
                <td>{log.explanation}</td>
                <td>{log.recommendation}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default LogList;
