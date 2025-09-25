from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import SQLAgent
from analyzer import UIAnalyzer
from schema import UIConfiguration
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory stores for agents and analyzers
sql_agents: dict[str, SQLAgent] = {}
ui_analyzer = UIAnalyzer() # This can be a singleton

class ConnectionRequest(BaseModel):
    db_path: str

class QueryRequest(BaseModel):
    session_id: str
    prompt: str

@app.post("/api/connect")
async def connect_to_db(request: ConnectionRequest):
    """
    Establishes a connection to the database and returns a session ID.
    """
    try:
        if not os.path.exists(request.db_path):
            raise HTTPException(status_code=400, detail=f"Database file not found at {request.db_path}")

        agent = SQLAgent(db_path=request.db_path)
        session_id = str(uuid.uuid4())
        sql_agents[session_id] = agent
        return {"status": "success", "session_id": session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create agent: {e}")

@app.post("/api/query", response_model=UIConfiguration)
async def handle_query(request: QueryRequest):
    """
    Handles a natural language query using a two-step process:
    1. SQL Agent generates and executes a query.
    2. UI Analyzer generates a UI configuration from the results.
    """
    agent = sql_agents.get(request.session_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Invalid session ID. Please connect first.")

    # Step 1: Get raw data from the SQL Agent
    raw_data_result = agent.query(request.prompt)
    if "error" in raw_data_result:
        raise HTTPException(status_code=500, detail=f"SQL Agent Error: {raw_data_result['error']}")

    raw_data = raw_data_result.get("result")

    # Step 2: Generate UI config from the UI Analyzer
    ui_config = ui_analyzer.generate_ui_config(query=request.prompt, data=raw_data)
    if not ui_config:
        raise HTTPException(status_code=500, detail="Failed to generate UI configuration from the LLM.")

    return ui_config