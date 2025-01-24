from typing import List
from pydantic import BaseModel
from models.citation import Citation
from models.citation_group import CitationGroup
from models.regulatory_info import RegulatoryInfo
from models.group_summary import GroupSummary


class State(BaseModel):
    citations: List[Citation] = []
    regulatory_info: List[RegulatoryInfo] = []
    groups: List[CitationGroup] = []
    summaries: List[GroupSummary] = []
