from typing import List
from pydantic import BaseModel, Field


class CitationGroupAttributes(BaseModel):
    functional_requirement: str = Field(..., description="The functional requirement for the group (e.g., 'Negative Reporting').")
    risk_level: str = Field(..., description="The risk level associated with the group (e.g., 'Medium-Risk').")
    penalty_details: str = Field(
        ..., description="Details about penalties or enforcement actions (e.g., 'Not specified, Administrative enforcement')."
    )
    frequency: str = Field(..., description="The frequency at which the requirement must be fulfilled (e.g., 'Annual').")
    automation_level: str = Field(
        ..., description="The level of automation required for compliance (e.g., 'Semi-automated (except Ohio, which is Manual)')."
    )


class Citation(BaseModel):
    citation_id: int = Field(..., description="A unique identifier for the citation.")
    citation_number: str = Field(
        ..., description="The official citation number or reference (e.g., '765 III. Comp. Stat. Ann. 1026/15-401(d)')."
    )
    citation_text: str = Field(..., description="The full text of the regulatory citation.")
    jurisdiction: str = Field(..., description="The jurisdiction (e.g., state or country) where the citation applies.")


# LLM Output Main class
class CitationGroupSummary(BaseModel):
    citation_group_id: int = Field(..., description="The unique identifier of the group.")
    citation_group_summary: str = Field(..., description="The generated compliance summary for the group.")
    citation_ids: List[int] = Field(..., description="A list of citation IDs referenced in the summary.")


class GroupSummaryList(BaseModel):
    summaries: List[CitationGroupSummary] = Field(..., description="A list of compliance summaries for different groups.")


# LLM Input Main class
class CitationGroup(BaseModel):
    citation_group_id: int = Field(..., description="A unique identifier for the group of citations.")
    citation_group_name: str = Field(
        ..., description="The name of the group, describing its theme or category (e.g., 'Medium-Risk Negative Reporting (General)')."
    )
    citations: List[Citation] = Field(..., description="A list of citations belonging to this group.")
    citation_group_attributes: CitationGroupAttributes = Field(
        ..., description="Attributes specific to the group, such as functional requirements, penalties, frequency, and automation level."
    )
