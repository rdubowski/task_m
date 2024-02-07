import React, { useState } from 'react';
import { encodeUrl, decodeUrl } from '../services/url';

import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';

function App() {
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [decodedUrl, setDecodedUrl] = useState('');
  const [encodedUrl, setEncodedUrl] = useState('');

  const handleEncode = async () => {
    const result = await encodeUrl(url.trim());
    setEncodedUrl(result);
  };

  const handleDecode = async () => {
    const result = await decodeUrl(shortUrl.trim());
    setDecodedUrl(result);
  };

  const defaultTheme = createTheme();

  return (
    <ThemeProvider theme={defaultTheme}>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Grid
  container
  spacing={0}
  direction="column"
  alignItems="center"
  justifyContent="center"
  sx={{ minHeight: '100vh' }}
>
            <Grid container spacing={2}>
              <Grid item xl={12}>
              <TextField
                  fullWidth
                  id="encodeUrl"
                  label="Url to encode"
                  name="encodeUrl"
                  value={url} onChange={e => setUrl(e.target.value)}
                />
        <Button
        onClick={handleEncode}
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 1, mb: 2}}
            >
              Encode
            </Button>
        {encodedUrl && <Typography variant="h5" gutterBottom>Encoded URL: {encodedUrl}</Typography>}
        </Grid>
        <Grid item xl={12}>
        <TextField
                  fullWidth
                  id="decodeUrl"
                  label="Url to decode"
                  name="decodeUrl"
                  value={shortUrl} onChange={e => setShortUrl(e.target.value)}
                />
       
        
        <Button
        onClick={handleDecode}
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 1 , mb: 2}}
            >
              Decode
            </Button>
            {decodedUrl && <Typography variant="h5" gutterBottom>Decoded URL: {decodedUrl}</Typography>}
            </Grid>
            </Grid>
            </Grid>
      </Container>
    </ThemeProvider>
  );
}


export default App;
