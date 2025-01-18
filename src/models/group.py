from pydantic import BaseModel, Field
from typing import List


class Group(BaseModel):
    """Represents a group of citations."""

    group_name: str = Field(description="The name of the group")
    citation_rowid_list: List[int] = Field(
        description="List of citation rowid in this group"
    )


class GroupList(BaseModel):
    group_list: List[Group] = Field(description="List of groups")
