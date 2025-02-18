from pydantic import BaseModel, Field
from typing import List


class Citation(BaseModel):
    citation_id: int = Field(..., description="Unique identifier for the citation.")
    citation_number: str = Field(..., description="The reference number of the citation.")
    # key_requirements: List[str] = Field(..., description="Extracted key compliance requirements from the citation.")
    is_mcr_level: bool = Field(..., description="Indicates whether the citation applies at the MCR level (no specific nuances).")


class AttributeGroup(BaseModel):
    attribute_name: str = Field(..., description="The name of the attribute derived from shared compliance nuances.")
    attribute_requirements: List[str] = Field(..., description="Key compliance requirements that define this attribute.")
    citations: List[Citation] = Field(default_factory=list, description="Citations that fall under this attribute.")


class MajorComplianceRequirement(BaseModel):
    mcr_name: str = Field(..., description="The name of the Major Compliance Requirement (MCR).")
    mcr_requirements: List[str] = Field(..., description="Key compliance obligations under this MCR.")
    attributes: List[AttributeGroup] = Field(default_factory=list, description="Grouped citations under attributes.")
    mcr_level_citations: List[Citation] = Field(
        default_factory=list,
        description="Citations that apply at the MCR level (no attributes required).",
    )
