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
    jurisdiction: str
    nuances: List[str]


class CitationWithTagsList(BaseModel):
    core_legal_obligation: str
    citations: List[CitationWithTags]


class CitationGroup(BaseModel):
    group_name: str
    description: str
    justification: str
    citation_ids: List[int]


class CitationGroupList(BaseModel):
    mcr_level_group: CitationGroup
    groups: List[CitationGroup]


class MajorComplianceRequirement(BaseModel):
    mcr_id: str
    citations: List[Citation]
