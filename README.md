# Giraffe

## Demo
Check us out on Devpost to see more details and the working demo of a generated AI video completely produced by our codebase: https://devpost.com/software/giraffe-study.


## Installation

To install the required dependencies, run the following commands in your terminal. 
You need to have pip and npm installed for the following commands.

```
pip install manim
pip install elevenlabs
pip install openai
pip install MoviePy
cd frontend
npm install
cd ..
cd backend
npm install
```

Finally, you need to have **active access keys** to the OpenAI and ElevenLabs API. 
Please insert the OpenAI key into line 4 of `logic/utils.py` and the ElevenLabs key into line 6 of `logic/narration/narration.py`.

## Running the Website

To run the website on both frontend and backend, you need to create two terminals.
Then, you run these commands in the first terminal:

```
cd frontend
npm run dev
```

After that, run the following commands in the second terminal:

```
cd backend
node server.js
```

## Raw Video Generation

You can run the raw video generation program by downloading the repo and running the following things in your terminal:

```
chmod +x super.sh
./super.sh
```

Developed by Artem Yushko, Maksym Bondarenko, and Veronika Kitsul
