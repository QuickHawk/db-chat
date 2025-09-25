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

# A Union of all possible UI elements, with the discriminator applied via Annotated.
UIElement = Annotated[
    Union[KPICard, BarChart, AnalysisText],
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