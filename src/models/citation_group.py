from pydantic import BaseModel, Field
from typing import List


class CitationGroup(BaseModel):
    """Represents a group of citations."""

    citation_group_name: str = Field(description="The name of the citations group")
    citation_ids: List[int] = Field(description="List of citation_id in this citation group")


class CitationGroupList(BaseModel):
    """Represents a list of citation groups."""

    citation_group_list: List[CitationGroup] = Field(description="List of citation groups")
