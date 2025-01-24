from pydantic import BaseModel, Field
from typing import List


class GroupSummary(BaseModel):
    """Represents a summary of a group of citations."""

    group_level: str = Field(
        description="Citation Grouping Level - Functional category / Product-level / State-level / General requirements"
    )
    group_criteria: str = Field(description="Unified summary for the group")
    citation_ids: List[int] = Field(description="List of citation_id in this group")
    group_summary: str = Field(description="Summary of the group")


# class SummaryList(BaseModel):
#     summary_list: List[GroupSummary] = Field(description="List of summaries")
