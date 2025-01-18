from pydantic import BaseModel, Field
from typing import List


class Summary(BaseModel):
    """Represents a summary of a group of citations."""

    group_id: str = Field(description="The ID of the group being summarized")
    group_summary: str = Field(description="The summary of the group")
    state_list: List[str] = Field(
        description="Additional state information for the group"
    )


class SummaryList(BaseModel):
    summary_list: List[Summary] = Field(description="List of summaries")
