# Giraffe

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

Finally, you need to have an active access key to the OpenAI API. 
Please insert it into line 4 of logic/utils.py

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
