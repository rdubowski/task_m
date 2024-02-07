import React, { useState } from 'react';
import { encodeUrl, decodeUrl } from '../services/url';

function App() {
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [decodedUrl, setDecodedUrl] = useState('');
  const [encodedUrl, setEncodedUrl] = useState('');

  const handleEncode = async () => {
    const result = await encodeUrl(url);
    setEncodedUrl(result);
  };

  const handleDecode = async () => {
    const result = await decodeUrl(shortUrl);
    setDecodedUrl(result.data?.short);
  };

  return (
    <div>
      <input type="text" value={url} onChange={e => setUrl(e.target.value)} placeholder="Enter URL to encode" />
      <button onClick={handleEncode}>Encode</button>
      {encodedUrl && <p>Encoded URL: {encodedUrl}</p>}

      <input type="text" value={shortUrl} onChange={e => setShortUrl(e.target.value)} placeholder="Enter URL to decode" />
      <button onClick={handleDecode}>Decode</button>
      {decodedUrl && <p>Decoded URL: {decodedUrl}</p>}
    </div>
  );
}


export default App;
