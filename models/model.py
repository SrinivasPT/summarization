from typing import List, Optional
from pydantic import BaseModel, Field


class Citation(BaseModel):
    citation_id: int = Field(..., description="A unique identifier for the citation.")
    citation_number: str = Field(
        ..., description="The official citation number or reference (e.g., '765 III. Comp. Stat. Ann. 1026/15-401(d)')."
    )
    citation_text: str = Field(..., description="The full text of the regulatory citation.")


class CitationWithAttributes(BaseModel):
    citation_id: int = Field(..., description="A unique identifier for the citation.", example=12345)
    citation_number: str = Field(
        ...,
        description="The official citation number or reference (e.g., '765 III. Comp. Stat. Ann. 1026/15-401(d)').",
        example="765 III. Comp. Stat. Ann. 1026/15-401(d)",
    )
    citation_text: str = Field(
        ...,
        description="The full text of the regulatory citation.",
        example="A financial institution must report suspicious activities within 30 days.",
    )
    functional_requirement: str = Field(
        ...,
        description="The functional requirement for the group (e.g., 'Negative Reporting', 'Data Retention').",
        example="Negative Reporting",
    )
    risk_level: str = Field(
        ...,
        description="The risk level associated with the citation. Possible values 'LOW', 'MEDIUM', 'HIGH'",
        example="MEDIUM",
    )
    applicable_entities: List[str] = Field(
        ..., description="Entity types subject to regulation (e.g., 'Banks', 'Credit Unions').", example=["Banks", "Credit Unions"]
    )
    jurisdiction: str = Field(..., description="Geographic or legal domain of enforcement (e.g., 'IL', 'NY').", example="IL")
    jurisdictional_nuances: Optional[List[str]] = Field(
        default_factory=list,
        description="List of jurisdictional variations or requirements.",
        example=["Exemptions for small businesses", "Additional reporting in NY"],
    )
    compliance_frequency: Optional[str] = Field(
        None, description="Primary compliance frequency (e.g., 'Annually', 'Quarterly', 'Per Report').", example="Quarterly"
    )
    compliance_frequency_nuances: Optional[List[str]] = Field(
        default_factory=list,
        description="List of nuances related to compliance frequency (e.g., deadlines, exceptions, variations).",
        example=["Deadline extended during holidays", "Quarterly reports due within 15 days"],
    )
    penalty_conditions: Optional[str] = Field(
        None,
        description="Enforcement mechanisms and exceptions (e.g., 'Fines up to $10,000').",
        example="Fines up to $10,000 for non-compliance",
    )
    penalty_conditions_nuances: Optional[List[str]] = Field(
        default_factory=list,
        description="List of penalty-related nuances (e.g., waivers, escalations).",
        example=["Waivers for first-time offenders", "Escalating fines for repeat violations"],
    )
    procedural_nuances: Optional[List[str]] = Field(
        default_factory=list,
        description="List of procedural requirements or exceptions (e.g., 'Written notice required').",
        example=["Written notice required", "Exemptions for non-profits"],
    )


class CitationWithAttributesList(BaseModel):
    data: List[CitationWithAttributes] = Field(..., description="A list of citations with additional attributes.")


class CitationGroup(BaseModel):
    citation_group_id: int = Field(..., description="A unique identifier for the group of citations.")
    citation_group_name: str = Field(
        ..., description="The name of the group, describing its theme or category (e.g., 'Medium-Risk Negative Reporting (General)')."
    )
    citation_ids: List[int] = Field(..., description="A list of citation ids belonging to this group.")
    functional_requirement: str = Field(..., description="The functional requirement for the group (e.g., 'Negative Reporting').")
    risk_level: str = Field(..., description="The risk level associated with the group (e.g., 'Medium-Risk').")
    penalty_details: str = Field(
        ..., description="Details about penalties or enforcement actions (e.g., 'Not specified, Administrative enforcement')."
    )
    frequency: str = Field(..., description="The frequency at which the requirement must be fulfilled (e.g., 'Annual').")
    automation_level: str = Field(
        ..., description="The level of automation required for compliance (e.g., 'Semi-automated (except Ohio, which is Manual)')."
    )


class CitationGroupList(BaseModel):
    data: List[CitationGroup] = Field(..., description="A list of citation groups with their respective attributes.")


class GenerateSummaryInput(BaseModel):
    citation_group_id: int = Field(..., description="A unique identifier for the group of citations.")
    citation_group_name: str = Field(
        ..., description="The name of the group, describing its theme or category (e.g., 'Medium-Risk Negative Reporting (General)')."
    )
    citation_ids: List[int] = Field(..., description="A list of citation ids belonging to this group.")
    functional_requirement: str = Field(..., description="The functional requirement for the group (e.g., 'Negative Reporting').")
    risk_level: str = Field(..., description="The risk level associated with the group (e.g., 'Medium-Risk').")
    penalty_details: str = Field(
        ..., description="Details about penalties or enforcement actions (e.g., 'Not specified, Administrative enforcement')."
    )
    frequency: str = Field(..., description="The frequency at which the requirement must be fulfilled (e.g., 'Annual').")
    automation_level: str = Field(
        ..., description="The level of automation required for compliance (e.g., 'Semi-automated (except Ohio, which is Manual)')."
    )
    citations: List[Citation] = Field(..., description="A list of citation referenced in the summary.")


class CitationGroupSummary(BaseModel):
    citation_group_id: int = Field(..., description="The unique identifier of the group.")
    citation_group_summary: str = Field(..., description="The generated compliance summary for the group.")


class GroupSummaryList(BaseModel):
    data: List[CitationGroupSummary] = Field(..., description="A list of compliance summaries for different groups.")
