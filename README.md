# Therapy Bot API

This project is a Therapy Bot API (AnVie) built with FastAPI. It is designed to provide a therapeutic chatbot experience, specifically tailored for university students.

## Features

*   **Chatbot Functionality:** Provides conversational therapy interactions.
*   **Scalable API:** Built with FastAPI for high performance and ease of use.
*   **CORS Enabled:** Configured to allow requests from different origins.

## Getting Started

### Prerequisites

*   Python 3.7+
*   pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone <https://github.com/LongNguyen1101/psycho_bot.git>
    cd <repository_folder>
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the API
    ```bash
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

    Replace `$PORT` with the desired port number.

## Project Structure

*   `main.py`: The main application file, initializes the FastAPI app and includes the chatbot router.
*   `app/routes/chatbot_router.py`: Defines the API endpoints related to the chatbot.
*   `app/services/crud.py`: Contains functions for Create, Read, Update, and Delete operations (likely for interacting with the database).
*   `app/database/mongo.py`: Handles the connection and operations with the MongoDB database.
*   `app/models/students_model.py`: Defines the data model for students.
*   `app/controllers/students_controller.py`: Contains the logic for handling student-related requests.
*   `app/agents/chain/`: Contains the logic for the chatbot's conversational flow and therapy chain.
*   `app/agents/core/`: Contains core components of the chatbot agent, including the graph, nodes, router, and state.
*   `app/agents/chain/prompts/`: Contains text files with prompts used by the chatbot.
