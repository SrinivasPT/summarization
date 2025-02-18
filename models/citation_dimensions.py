from typing import List, Optional
from pydantic import BaseModel, Field


class CitationDimensions(BaseModel):
    citation_id: int = Field(..., description="Unique identifier for the citation")
    citation_number: str = Field(..., description="Official citation number")
    # citation_text: str = Field(..., description="Full text of the citation")
    requirements: List[str] = Field(..., description="Specific compliance requirement")


class CitationDimensionsList(BaseModel):
    data: List[CitationDimensions] = Field(..., description="List of citations with their dimensions")
