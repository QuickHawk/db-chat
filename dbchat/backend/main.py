from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import DBAgent
from analyzer import UIGenerator
from schema import UIConfiguration
import uuid

app = FastAPI()

# A simple in-memory store to hold agent instances for this PoC
agents: dict[str, DBAgent] = {}

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
        agent = DBAgent(db_path=request.db_path)
        session_id = str(uuid.uuid4())
        agents[session_id] = agent
        return {"status": "success", "session_id": session_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to connect to database: {e}")

@app.post("/api/query", response_model=UIConfiguration)
async def handle_query(request: QueryRequest):
    """
    Handles a natural language query, gets raw data, analyzes it,
    and returns a full UI configuration.
    """
    agent = agents.get(request.session_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Invalid session ID. Please connect first.")

    raw_data = agent.query(request.prompt)

    if raw_data and "error" in raw_data[0]:
        raise HTTPException(status_code=400, detail=raw_data[0]["error"])

    # Analyze the data and generate the UI configuration
    ui_generator = UIGenerator(prompt=request.prompt, data=raw_data)
    ui_config = ui_generator.generate_ui()

    return ui_config