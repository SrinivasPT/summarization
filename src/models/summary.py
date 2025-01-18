from typing import List
from pydantic import BaseModel


class Summary(BaseModel):
    group_id: str
    group_summary: str
    state_list: List[str]  # Additional state information if needed


class SummaryList(BaseModel):
    summary_list: List[Summary]
