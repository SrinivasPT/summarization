from pydantic import BaseModel
from typing import List, Optional


class EmbeddableModel(BaseModel):
    embedding: Optional[List[float]] = None


class EmbeddingRequest(BaseModel):
    objects: List[dict]
    field_name: str


class EmbeddingResponse(BaseModel):
    objects: List[dict]
