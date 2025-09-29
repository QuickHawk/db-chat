import os
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SQLAgent:
    def __init__(self, db_path: str):
        """
        Initializes the SQL Agent with a connection to the database and the LLM.
        """
        # Ensure the API key is loaded
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        self.db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
        self.llm = ChatGoogleGenerativeAI(model=os.environ['GOOGLE_MODEL'], temperature=0)

        # Create the SQL agent using LangChain's create_sql_agent
        self.agent_executor = create_sql_agent(
            llm=self.llm,
            db=self.db,
            agent_type="openai-tools", # This type is compatible with Gemini
            verbose=True # Set to True for debugging
        )

    def query(self, prompt: str) -> dict:
        """
        Takes a natural language prompt, generates and executes an SQL query,
        and returns the result.
        """
        try:
            # The agent executor returns a dictionary with an 'output' key
            result = self.agent_executor.invoke({"input": prompt})
            return {"result": result.get("output", "No result found.")}
        except Exception as e:
            # Handle potential errors from the agent or LLM
            return {"error": str(e)}