from pydantic import BaseModel, Field
from typing import List


class Citation(BaseModel):
    citation_id: int
    citation_number: str
    citation_text: str


class StandardCitation(BaseModel):
    citation_id: int
    citation_number: str
    citation_text: str
    jurisdiction: str
    review_notes: List[str]


class StandardCitationList(BaseModel):
    citations: List[StandardCitation]


class CitationWithTags(BaseModel):
    citation_id: int
    citation_number: str
    citation_text: str
    jurisdiction: str
    core_legal_obligation: str
    specific_compliance_details: List[str]
    review_notes: List[str]


class CitationWithTagsList(BaseModel):
    citations: List[CitationWithTags]


class CitationWithCategory(BaseModel):
    citation_id: int
    citation_number: str
    citation_text: str
    jurisdiction: str
    core_legal_obligation: str
    specific_compliance_details: List[str]
    category: str
    sub_category: str
    review_notes: List[str]


class CitationWithCategoryList(BaseModel):
    citations: List[CitationWithCategory]


class MajorComplianceRequirement(BaseModel):
    mcr_id: str
    citations: List[Citation]
