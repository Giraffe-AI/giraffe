const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');

const app = express();

// Middleware for parsing JSON bodies
app.use(express.json());

// Enable all CORS requests - be more restrictive if needed
app.use(cors());

// Route for handling the JSON data and running the bash script
app.post('/', (req, res) => {
  // Assuming your JSON data is used in some way when running the script
  const jsonData = req.body;

  // Replace 'path/to/script.sh' with your script's actual path
  exec('bash ../hello.sh', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).json({ error: `exec error: ${error}` });
    }
    // Send script output as response
    res.json({ output: stdout });
  });

  console.log(jsonData);
});

// Start the server
const PORT = 3001; // Use any port not used by your React app
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
