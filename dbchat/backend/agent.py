import sqlite3
from typing import List, Dict, Any

# A mock "LLM" that maps natural language questions to SQL queries.
# In a real application, this would be a call to an actual LLM.
QUERY_MAPPING = {
    "how much is the story points for this sprint?": "SELECT SUM(story_points) FROM sprints;",
    "analyse the expenses of this month?": "SELECT category, SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') GROUP BY category;",
    "what are the top 5 most expensive items this month?": "SELECT item, amount FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') ORDER BY amount DESC LIMIT 5;"
}

class DBAgent:
    def __init__(self, db_path: str):
        """
        Initializes the agent with a path to the SQLite database.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        # Use a dictionary cursor to get results as a list of dicts
        self.conn.row_factory = sqlite3.Row

    def get_sql_from_prompt(self, prompt: str) -> str:
        """
        Simulates an LLM call to get an SQL query from a natural language prompt.
        """
        # Use a case-insensitive lookup
        return QUERY_MAPPING.get(prompt.lower().strip(), "SELECT 'Invalid prompt. Please try one of the known questions.'")

    def execute_sql(self, sql: str) -> List[Dict[str, Any]]:
        """
        Executes the given SQL query and returns the results.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            # Convert rows to a list of dictionaries
            results = [dict(row) for row in cursor.fetchall()]
            return results
        except sqlite3.Error as e:
            return [{"error": str(e)}]

    def query(self, prompt: str) -> List[Dict[str, Any]]:
        """
        Takes a natural language prompt, converts it to SQL, executes it,
        and returns the results.
        """
        sql_query = self.get_sql_from_prompt(prompt)
        results = self.execute_sql(sql_query)
        return results

    def close(self):
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()