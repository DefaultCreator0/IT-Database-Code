import React, { useState, useEffect } from 'react';

function App() {
  const [getMessage, setGetMessage] = useState('');
  const [postMessage, setPostMessage] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/Fetch')
      .then(res => res.json())
      .then(data => setGetMessage(data.message));
  }, []);

  const handlePostData = () => {
    fetch('http://localhost:5000/post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: postMessage }),
    })
    .then(res => res.json())
    .then(data => setResponse(data.received));
  };

  return (
    <div>
      <p>{getMessage}</p>
      <input
        type="text"
        value={postMessage}
        onChange={(e) => setPostMessage(e.target.value)}
      />
      <button onClick={handlePostData}>Send Data</button>
      <p>{response}</p>
    </div>
  );
}

export default App;