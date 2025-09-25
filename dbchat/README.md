# DBChat - Generative UI Proof of Concept

This project is a Proof of Concept for a "Generative UI" application. It allows a user to connect to a database and ask questions in natural language. The backend agent analyzes the request and generates a dynamic UI configuration, which the frontend then renders in real-time.

## Project Structure

-   `backend/`: Contains the Python FastAPI server, the natural language agent (simulated), and database connection logic.
-   `frontend/`: Contains the React application that handles user input and dynamically renders the UI based on the backend's response.

---

## How to Run This Project

### Prerequisites

-   Python 3.10+
-   Node.js and npm

### 1. Backend Setup

First, set up and run the Python backend server.

```bash
# Navigate to the backend directory
cd dbchat/backend

# Create a virtual environment
# (Using virtualenv is recommended if venv has issues)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# The repository does not have a requirements.txt, so let's install them manually
pip install fastapi uvicorn[standard] langchain langchain-community sqlalchemy

# Create the sample database for testing
python3 create_sample_db.py

# Run the backend server
uvicorn main:app --host 127.0.0.1 --port 8000
```

The backend server will be running at `http://127.0.0.1:8000`.

### 2. Frontend Setup

In a new terminal, set up and run the React frontend.

```bash
# Navigate to the frontend directory
cd dbchat/frontend

# Install dependencies
npm install

# Run the frontend development server
npm run dev
```

The frontend will be available at `http://localhost:5173` (or another port if 5173 is busy).

### 3. Using the Application

1.  **Open your browser** to the frontend URL (e.g., `http://localhost:5173`).
2.  **Connect to the database.** In the input field, provide the path to the sample database. Since the backend and frontend are on the same machine, you can use a relative path from the `backend` directory: `sample_data.db`.
3.  **Click "Connect".**
4.  **Ask a question.** Once connected, use the chat input to ask one of the hardcoded questions:
    *   `How much is the story points for this sprint?`
    *   `Analyse the expenses of this month?`
    *   `What are the top 5 most expensive items this month?`
5.  **View the dynamic UI.** The frontend will render a UI with charts and cards based on the backend's response.