import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schema import UIConfiguration
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class UIAnalyzer:
    def __init__(self):
        """
        Initializes the UI Analyzer with the LLM and a JSON output parser.
        """
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        self.llm = ChatGoogleGenerativeAI(model=os.environ.get('GOOGLE_MODEL', 'gemini-1.5-pro'), temperature=0)
        self.parser = JsonOutputParser(pydantic_object=UIConfiguration)

    def _get_prompt_template(self) -> ChatPromptTemplate:
        """
        Creates the detailed prompt for the LLM to generate the UI configuration.
        """
        prompt = """
        You are an expert data analyst and UI designer. Your task is to analyze raw data and a user's query to generate a dynamic and insightful user interface.

        You must generate a JSON object that strictly follows this Pydantic schema:
        {schema}

        Here are the available UI components you can use:
        - `kpi_card`: Ideal for displaying single, important numbers (e.g., totals, counts, averages).
        - `bar_chart`: Perfect for comparing values across different categories.
        - `line_chart`: Use this to show trends over a continuous variable, like time.
        - `pie_chart`: Excellent for displaying the proportions of a whole. Use when categories sum to 100%.
        - `data_table`: Use this to display raw, tabular data when a chart isn't appropriate or when the user asks for the data itself.
        - `scatter_plot`: Use this to visualize the relationship and correlation between two different numerical variables.
        - `analysis_text`: Use this for providing summaries, insights, or lists of data that don't fit other formats.

        Analyze the user's query and the resulting data to decide which UI components are most appropriate. Be creative and insightful. You can combine multiple components to build a rich dashboard.

        User's Query:
        {query}

        Raw Data (from SQL query):
        {data}

        Now, generate the UI configuration as a valid JSON object.
        """
        return ChatPromptTemplate.from_template(
            prompt,
            partial_variables={"schema": self.parser.get_format_instructions()}
        )

    def generate_ui_config(self, query: str, data: str) -> UIConfiguration:
        """
        Takes the user's query and raw data, and returns a UIConfiguration object.
        """
        prompt_template = self._get_prompt_template()
        chain = prompt_template | self.llm | self.parser

        try:
            ui_config = chain.invoke({"query": query, "data": str(data)})
            return ui_config
        except Exception as e:
            # In a real app, you might want to have a fallback or retry mechanism
            print(f"Error generating UI config: {e}")
            return None