# A.I.Homework
Alkalmazott Mesterséges Intelligencia a Gyakorlatban Kurzus

# Interview Chatbot Project

This project is a job interview preparation chatbot built with FastAPI and OpenAI's GPT model. The chatbot helps users prepare for job interviews by generating relevant questions based on the user's input. It simulates an interviewer's role, asking questions about the job title, the user's qualifications, and providing feedback at the end of the interview.

## Project Structure

- **Backend**: The backend is built with **FastAPI**, which handles the API requests for generating interview questions and receiving user responses. The backend also communicates with the OpenAI GPT model to generate intelligent responses.
- **Frontend**: The frontend is built using **HTML**, **CSS**, and **JavaScript**. It provides an interface for the user to interact with the chatbot.

## Features

- Generate interview questions based on a given job title or topic.
- Allow the user to answer the generated questions.
- Provide feedback at the end of the interview based on user responses.
- Simulate a real-life job interview scenario with automatic follow-up questions.

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Tomi1229/interview-chatbot.git

2. Install the dependencies:
    cd interview-chatbot/backend
    pip install -r requirements.txt

3. Set the OpenAI API key:
    export OPENAI_API_KEY="your_api_key"

4. Run the FastAPI backend:
    uvicorn app.main:app --reload

### Frontend Setup

Open the index.html file in your browser.

### Usage

Start the backend server and open the index.html file in a browser.
Enter your job title or interview topic, and the chatbot will ask relevant questions.
Answer the questions, and the chatbot will provide feedback.

### Contributing

Feel free to fork the repository, make changes, and create pull requests.

### Acknowledgments

This project was created as part of a university course on applied artificial intelligence models.