from typing import List, Dict, Any
from schema import UIConfiguration, KPICard, KPICardData, BarChart, BarChartData, AnalysisText, AnalysisTextData

class UIGenerator:
    def __init__(self, prompt: str, data: List[Dict[str, Any]]):
        self.prompt = prompt.lower().strip()
        self.data = data

    def generate_ui(self) -> UIConfiguration:
        """
        Analyzes the prompt and data to generate a UI configuration.
        This is a rule-based system for the PoC.
        """
        elements = []

        # Rule 1: Handle single-value results (e.g., SUM, COUNT)
        if "how much" in self.prompt and len(self.data) == 1:
            first_row = self.data[0]
            # Assumes the first column is the value
            value_key = list(first_row.keys())[0]
            value = first_row[value_key]

            kpi_card = KPICard(
                data=KPICardData(
                    title="Result",
                    value=str(value),
                    description=f"Based on your query: '{self.prompt}'"
                ),
                is_highlighted=True,
                size="medium"
            )
            elements.append(kpi_card)

        # Rule 2: Handle categorical analysis (e.g., GROUP BY)
        elif "analyse" in self.prompt and len(self.data) > 0:
            # Assumes first column is category, second is value
            keys = list(self.data[0].keys())
            category_key, value_key = keys[0], keys[1]

            bar_chart = BarChart(
                data=BarChartData(
                    title="Expense Analysis",
                    labels=[str(row[category_key]) for row in self.data],
                    values=[float(row[value_key]) for row in self.data]
                ),
                size="large"
            )
            elements.append(bar_chart)

            analysis_text = AnalysisText(
                data=AnalysisTextData(
                    title="Summary",
                    text="This chart shows the breakdown of expenses by category for the current month."
                )
            )
            elements.append(analysis_text)

        # Rule 3: Handle lists (e.g., top 5)
        elif "top 5" in self.prompt and len(self.data) > 0:
            # Creates a simple text block with the list
            text_content = "Here are the top 5 items:\n"
            for row in self.data:
                item = row.get('item', 'N/A')
                amount = row.get('amount', 'N/A')
                text_content += f"- {item}: ${amount}\n"

            analysis_text = AnalysisText(
                data=AnalysisTextData(
                    title="Top 5 Most Expensive Items",
                    text=text_content
                ),
                size="large"
            )
            elements.append(analysis_text)

        # Default fallback
        else:
            elements.append(AnalysisText(data=AnalysisTextData(title="Query Result", text=str(self.data))))

        return UIConfiguration(elements=elements)