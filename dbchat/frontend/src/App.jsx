import React, { useState } from 'react';
import { connectToDatabase, sendQuery } from './api';
import ComponentMapper from './components/ComponentMapper';
import './App.css';

function App() {
  // State management
  const [dbPath, setDbPath] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [prompt, setPrompt] = useState('');
  const [uiConfig, setUiConfig] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handlers
  const handleConnect = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      const response = await connectToDatabase(dbPath);
      setSessionId(response.data.session_id);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to connect to the database.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuery = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    setUiConfig(null);
    try {
      const response = await sendQuery(sessionId, prompt);
      setUiConfig(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred while fetching the data.');
    } finally {
      setIsLoading(false);
      setPrompt('');
    }
  };

  // Render logic
  if (!sessionId) {
    return (
      <div className="App connection-view">
        <h1>DBChat: Connect to Database</h1>
        <form onSubmit={handleConnect} className="connection-form">
          <input
            type="text"
            value={dbPath}
            onChange={(e) => setDbPath(e.target.value)}
            placeholder="Enter path to SQLite database file"
            required
          />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Connecting...' : 'Connect'}
          </button>
        </form>
        {error && <p className="error-message">{error}</p>}
      </div>
    );
  }

  return (
    <div className="App chat-view">
      <header>
        <h1>DBChat</h1>
        <p>Connected to: {dbPath}</p>
      </header>
      <main className="chat-main">
        <div className="response-area">
          {isLoading && <p>Loading...</p>}
          {error && <p className="error-message">{error}</p>}
          {uiConfig && (
            <div className={`dynamic-ui-container ${uiConfig.layout}`}>
              {uiConfig.elements.map((element, index) => (
                <ComponentMapper key={index} element={element} />
              ))}
            </div>
          )}
        </div>
        <form onSubmit={handleQuery} className="prompt-form">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Ask a question about your data..."
            required
          />
          <button type="submit" disabled={isLoading}>
            Send
          </button>
        </form>
      </main>
    </div>
  );
}

export default App;