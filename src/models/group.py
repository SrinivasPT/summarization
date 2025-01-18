from typing import List
from pydantic import BaseModel


class Group(BaseModel):
    group_name: str
    citation_rowid_list: List[int]


class GroupList(BaseModel):
    group_list: List[Group]
