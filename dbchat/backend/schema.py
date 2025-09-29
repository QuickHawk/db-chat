from pydantic import BaseModel, Field
from typing import List, Union, Literal, Dict, Any, Annotated

# --- Data Models for Specific UI Elements ---

class KPICardData(BaseModel):
    title: str
    value: str
    description: str | None = None

class BarChartData(BaseModel):
    title: str
    labels: List[str]
    values: List[float]

class AnalysisTextData(BaseModel):
    title: str
    text: str

# --- Generic UI Element Models ---

class KPICard(BaseModel):
    type: Literal["kpi_card"] = "kpi_card"
    data: KPICardData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "medium"

class BarChart(BaseModel):
    type: Literal["bar_chart"] = "bar_chart"
    data: BarChartData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "large"

class AnalysisText(BaseModel):
    type: Literal["analysis_text"] = "analysis_text"
    data: AnalysisTextData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "medium"

# --- New Component Models ---

class LineChartData(BaseModel):
    title: str
    x_axis_label: str
    y_axis_label: str
    lines: List[Dict[str, Any]] # e.g., [{'name': 'Sales', 'points': [{'x': 1, 'y': 10}]}]

class LineChart(BaseModel):
    type: Literal["line_chart"] = "line_chart"
    data: LineChartData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "large"

class PieChartData(BaseModel):
    title: str
    segments: List[Dict[str, Any]] # e.g., [{'name': 'USA', 'value': 400}]

class PieChart(BaseModel):
    type: Literal["pie_chart"] = "pie_chart"
    data: PieChartData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "medium"

class DataTableData(BaseModel):
    title: str
    headers: List[str]
    rows: List[List[Any]]

class DataTable(BaseModel):
    type: Literal["data_table"] = "data_table"
    data: DataTableData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "large"

class ScatterPlotData(BaseModel):
    title: str
    x_axis_label: str
    y_axis_label: str
    points: List[Dict[str, Any]] # e.g., [{'x': 10, 'y': 20}]

class ScatterPlot(BaseModel):
    type: Literal["scatter_plot"] = "scatter_plot"
    data: ScatterPlotData
    is_highlighted: bool = False
    size: Literal["small", "medium", "large"] = "large"


# A Union of all possible UI elements, with the discriminator applied via Annotated.
UIElement = Annotated[
    Union[KPICard, BarChart, AnalysisText, LineChart, PieChart, DataTable, ScatterPlot],
    Field(discriminator="type")
]

# --- Top-Level UI Configuration Schema ---

class UIConfiguration(BaseModel):
    """
    The definitive schema for the dynamic UI configuration sent from the backend to the frontend.
    """
    theme: Literal["dark", "light"] = "dark"
    layout: Literal["dashboard", "list"] = "dashboard"
    elements: List[UIElement]