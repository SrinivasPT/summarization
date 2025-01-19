from typing import List, Dict
from pydantic import BaseModel
from models.citation import Citation
from models.group import Group
from models.summary import GroupSummary


class State(BaseModel):
    citations: List[Citation] = []
    groups: List[Group] = []
    summaries: List[GroupSummary] = []
