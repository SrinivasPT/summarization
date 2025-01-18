from pydantic import BaseModel


class Citation(BaseModel):
    rowid: int
    issuing_authority: str
    citation_number: str
    citation_text: str
    group_id: str = None
