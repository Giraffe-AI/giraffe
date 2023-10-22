const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');

const app = express();

// middleware for parsing JSON bodies
app.use(express.json());
app.use(cors());

let currentVideo = '';

// returns the video status to the frontend
app.get('/video-status', (req, res) => {
  res.json({ video: currentVideo });
});

// handles the JSON data and running the bash script
app.post('/', (req, res) => {
  const jsonData = req.body;

  exec('bash ../logic/super.sh', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).json({ error: `exec error: ${error}` });
    }
    // sends script output as response
    res.json({ output: stdout });
  });

  console.log(jsonData);
});

// handles the request from the bash script
app.post('/script-started', (req, res) => {
  let { code, video } = req.body;

  if (code === "200") {
    console.log(`Video processing has started, file name: ${video}`);
    currentVideo = 'temp';
    res.json({ message: 'Received the video info successfully.' });
  } else {
    console.error('Something went wrong in the video receiving.');
    res.status(500).json({ error: 'There was an error in the video receiving.' });
  }
});

// handles the request from the bash script
app.post('/script-complete', (req, res) => {
  let { code, video } = req.body;

  if (code === "200") {
    console.log(`Video processing complete, file name: ${video}`);
    currentVideo = video;
    res.json({ message: 'Received the video info successfully.' });
  } else {
    console.error('Something went wrong in the video processing.');
    res.status(500).json({ error: 'There was an error in the video processing.' });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
