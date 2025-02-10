from pydantic import BaseModel, Field
from typing import List, Optional


class Citation(BaseModel):
    citation_id: int = Field(..., description="Unique identifier for the citation.")
    citation_number: str = Field(..., description="The reference number of the citation.")
    key_requirements: List[str] = Field(..., description="Extracted key compliance requirements from the citation.")


class CitationsGroup(BaseModel):
    group_requirements: List[str] = Field(..., description="List of key compliance requirements for this group.")
    group_name: str = Field(..., description="Derive the group name from the shared requirements.")
    citations: List[Citation] = Field(default_factory=list, description="List of citations that belong to this group.")


class CitationGrouping(BaseModel):
    data: List[CitationsGroup] = Field(default_factory=list, description="List of groupings of citations")
