from typing import List, Optional
from pydantic import BaseModel, Field


class PenaltyConditions(BaseModel):
    penalty_amount: Optional[str] = Field(None, description="Monetary penalty amount per violation")
    enforcement_type: Optional[str] = Field(None, description="Type of enforcement action (e.g., 'Civil', 'Criminal', 'Administrative')")


class ComplianceAttributes(BaseModel):
    functional_requirement: str = Field(
        ...,
        description="Core regulatory obligation (e.g., 'Negative Reporting', 'Examination Response')",
        example="Negative Reporting",
    )
    jurisdiction: str = Field(..., description="Geographic/legal domain of enforcement (e.g., 'IL', 'NY')", example="Illinois")
    applicable_entities: List[str] = Field(..., description="Entity types subject to regulation", example=["Business Associations"])
    risk_level: str = Field(..., description="Risk level (High, Medium, Low)", example="Medium")
    penalty_conditions: Optional[PenaltyConditions] = Field(None, description="Enforcement mechanisms and exceptions")
    penalty_conditions_nuances: Optional[List[str]] = Field(None, description="List of penalty-related nuances")
    procedural_nuances: Optional[List[str]] = Field(
        None,
        description="List of procedural requirements or nuances as strings",
    )
    jurisdictional_nuances: Optional[List[str]] = Field(
        None,
        description="List of jurisdictional variations or requirements as strings",
    )
    compliance_frequency: Optional[str] = Field(
        None,
        description="Primary compliance frequency (e.g., 'Annually', 'Quarterly', 'Per Report')",
    )
    compliance_frequency_nuances: Optional[List[str]] = Field(
        None,
        description="List of nuances related to compliance frequency (e.g., deadlines, exceptions, variations)",
    )


class RegulatoryInfo(BaseModel):
    citation_number: str = Field(..., description="The legal citation number, e.g., '765 III. Comp. Stat. Ann. 1026/15-401(d)'.")
    summary: str = Field(..., description="A summary of the regulation's requirements or restrictions.")
    compliance_attributes: ComplianceAttributes = Field(..., description="Structured compliance implementation metadata")


class RegulatoryInfoResponse(BaseModel):
    regulatory_info: Optional[List[RegulatoryInfo]] = Field(None, description="A list of regulatory information entries.")
