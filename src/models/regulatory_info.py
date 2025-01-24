from typing import List, Optional
from pydantic import BaseModel, Field


class TemporalContext(BaseModel):
    effective_date: Optional[str] = Field(
        None, description="The effective date of the regulation, e.g., 'YYYY-MM-DD' or 'N/A' if not applicable."
    )
    expiration_date: Optional[str] = Field(
        None, description="The expiration date of the regulation, e.g., 'YYYY-MM-DD' or 'N/A' if not applicable."
    )


class Attributes(BaseModel):
    Functional_Requirement: Optional[str] = Field(
        None, description="The functional requirement imposed by the regulation, e.g., 'Disclosure restriction'."
    )
    Applicable_Entity: Optional[str] = Field(
        None, description="The type of entity to which the regulation applies, e.g., 'Delinquent taxpayer or debtor'."
    )
    Action_Type: Optional[str] = Field(
        None, description="The type of action required or restricted by the regulation, e.g., 'Notification and withholding'."
    )
    Penalty_Exception_Conditions: Optional[str] = Field(
        None,
        description="Details of any penalties, exceptions, or conditions related to the regulation, e.g., 'No liability for non-disclosure'.",
    )
    Regulatory_Source: Optional[str] = Field(None, description="The source of the regulation, e.g., 'Statutory', 'Administrative', etc.")
    Temporal_Context: Optional[TemporalContext] = Field(
        None, description="The time-related context of the regulation, including effective and expiration dates."
    )
    Industry_Product_Applicability: Optional[str] = Field(
        None, description="The industries or products to which the regulation applies, e.g., 'General financial services'."
    )
    Risk_Level: Optional[str] = Field(
        None, description="The level of risk associated with non-compliance, e.g., 'Low', 'Medium', or 'High'."
    )
    Compliance_Effort: Optional[str] = Field(
        None, description="The effort required to comply with the regulation, e.g., 'Low', 'Medium', or 'High'."
    )
    Related_Citations: Optional[List[str]] = Field(None, description="A list of related citations or regulations, if any.")
    Exemptions: Optional[str] = Field(None, description="Details of any exemptions to the regulation, e.g., 'N/A' if no exemptions apply.")
    Citation_Context: Optional[str] = Field(
        None, description="The context in which the citation is relevant, e.g., 'Disclosure of delinquent taxpayer information'."
    )
    Penalty_Details: Optional[str] = Field(
        None, description="Details of penalties for violating the regulation, e.g., 'No penalty specified for disclosure violations'."
    )
    Frequency_of_Compliance_Action: Optional[str] = Field(
        None, description="How often compliance actions are required, e.g., 'Compliance required per information request'."
    )
    Interaction_with_Other_Laws: Optional[str] = Field(
        None, description="How the regulation interacts with other laws, e.g., 'Must align with federal privacy laws'."
    )
    Applicability_Exceptions: Optional[str] = Field(
        None, description="Any exceptions to the applicability of the regulation, e.g., 'N/A' if no exceptions apply."
    )
    Risk_of_Non_Compliance: Optional[str] = Field(
        None, description="The risk level associated with non-compliance, e.g., 'Medium due to legal obligations'."
    )
    Affected_Stakeholders: Optional[str] = Field(
        None, description="The stakeholders affected by the regulation, e.g., 'Financial institutions and account holders'."
    )
    Data_Sensitivity: Optional[str] = Field(
        None, description="The sensitivity level of the data covered by the regulation, e.g., 'Moderate sensitivity: taxpayer information'."
    )


class RegulatoryInfo(BaseModel):
    citation_id: Optional[int] = Field(None, description="A unique identifier for the citation.")
    citation_number: Optional[str] = Field(None, description="The legal citation number, e.g., 'Ky. Rev. Stat. § 131.676(1)'.")
    issuing_authority: Optional[str] = Field(
        None, description="The authority or entity that issued the regulation, e.g., 'Kentucky Government'."
    )
    summary: Optional[str] = Field(None, description="A summary of the regulation's requirements or restrictions.")
    attributes: Optional[Attributes] = Field(
        None, description="The attributes providing detailed context and requirements of the regulation."
    )


class RegulatoryInfoResponse(BaseModel):
    regulatory_info: Optional[List[RegulatoryInfo]] = Field(None, description="A list of regulatory information entries.")
