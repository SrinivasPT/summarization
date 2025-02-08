from pydantic import BaseModel, Field
from typing import List, Optional


class LegalRegulatory(BaseModel):
    regulatory_authority: str = Field(..., description="Regulatory body enforcing the citation")
    jurisdiction: str = Field(..., description="State, national, or international jurisdiction")
    law_reference: str = Field(..., description="Legal statute, regulation, or rule reference")
    enforcement_mechanism: Optional[str] = Field(None, description="How compliance is enforced (e.g., audits, penalties)")


class ComplianceRisk(BaseModel):
    filing_requirements: str = Field(..., description="What must be filed or reported")
    thresholds: Optional[str] = Field(None, description="Financial or operational thresholds triggering compliance")
    due_diligence: Optional[str] = Field(None, description="Required compliance procedures (e.g., KYC, AML)")
    penalties: Optional[str] = Field(None, description="Consequences of non-compliance")


class OperationalProcedural(BaseModel):
    reporting_frequency: str = Field(..., description="How often reports must be filed (e.g., annual, quarterly)")
    approval_required: Optional[str] = Field(None, description="Who must approve or certify compliance")
    record_retention: Optional[str] = Field(None, description="Duration for which records must be kept")
    internal_controls: Optional[str] = Field(None, description="Required internal compliance controls")


class BusinessProductSpecific(BaseModel):
    business_unit: str = Field(..., description="Which business unit is affected (e.g., retail banking, asset management)")
    product_applicability: str = Field(..., description="Which financial products/services are impacted")
    transaction_impact: Optional[str] = Field(None, description="Transaction types affected by the citation")


class TechnologyDataGovernance(BaseModel):
    data_security: Optional[str] = Field(None, description="Any data privacy or security requirements")
    digital_banking: Optional[str] = Field(None, description="Does it impact digital banking operations?")
    it_infrastructure: Optional[str] = Field(None, description="Any technology or system requirements")
    vendor_compliance: Optional[str] = Field(None, description="Third-party/vendor obligations")


class CustomerMarketImpact(BaseModel):
    consumer_protection: Optional[str] = Field(None, description="How it impacts customers' rights or protections")
    market_stability: Optional[str] = Field(None, description="Does it impact financial market stability?")
    transparency: Optional[str] = Field(None, description="Any required public disclosures or transparency rules")


class CitationDimensions(BaseModel):
    citation_id: int = Field(..., description="Unique identifier for the citation")
    citation_number: str = Field(..., description="Official citation number")
    citation_text: str = Field(..., description="Full text of the citation")
    # Dimensions
    legal_regulatory: LegalRegulatory
    compliance_risk: ComplianceRisk
    operational_procedural: OperationalProcedural
    business_product_specific: BusinessProductSpecific
    technology_data_governance: TechnologyDataGovernance
    customer_market_impact: CustomerMarketImpact
