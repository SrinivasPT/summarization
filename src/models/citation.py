from pydantic import BaseModel, Field


class Citation(BaseModel):
    citation_id: int = Field(description="The unique identifier for the citation.")
    citation_issuing_authority: str = Field(
        description="The authority or organization that issued the citation, e.g., 'Kentucky Government'."
    )
    citation_number: str = Field(description="The legal citation number, e.g., 'Ky. Rev. Stat. § 131.676(1)'.")
    citation_text: str = Field(description="The full text or description of the citation, providing context or details.")
    citation_group_id: str = Field(None, description="An optional identifier for the group or category this citation belongs to.")
