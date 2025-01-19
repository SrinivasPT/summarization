from pydantic import BaseModel, Field
from typing import List


class GroupSummary(BaseModel):
    """Represents a summary of a group of citations."""

    group_summary: str = Field(description="Unified summary for the group")
    citation_rowid_list: List[int] = Field(
        description="List of citation rowid in this group"
    )


# class SummaryList(BaseModel):
#     summary_list: List[GroupSummary] = Field(description="List of summaries")
