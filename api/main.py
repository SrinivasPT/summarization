import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # Add this import
from models import Citation, CitationWithAttributes, CitationGroupSummary
from agents.extraction_agent.logic import generate_citation_attributes
from agents.grouping_agent.logic import generate_citation_groups
from agents.summarization_agent.logic import generate_summary_for_all_group
from models.citation_dimensions import CitationDimensions
from models.citation_group import CitationGrouping
from models.model import GenerateSummaryInput
from models.embedding_model import EmbeddingRequest, EmbeddingResponse
from utils.embedding_util import add_embeddings_to_objects

app = FastAPI(title="Citation Analysis API", description="API for citation extraction, grouping and summarization")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-embeddings", response_model=EmbeddingResponse)
async def generate_embeddings(request: EmbeddingRequest):
    try:
        object_dicts = [obj.model_dump() if isinstance(obj, BaseModel) else obj for obj in request.objects]
        objects_with_embeddings = add_embeddings_to_objects(object_dicts, request.field_name)

        if not objects_with_embeddings:
            raise HTTPException(status_code=500, detail="Failed to generate embeddings")
        return EmbeddingResponse(objects=objects_with_embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/citations/{id}", response_model=List[Citation])
async def get_citations(id: str):
    try:
        file_path = os.path.join("data", f"{id}.json")
        with open(file_path, "r") as file:
            data = json.load(file)
            return [Citation.model_validate(item) for item in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract-citation-attributes", response_model=List[CitationDimensions])
async def extract_citations(citations: List[Citation]):
    try:
        citations_with_attributes = generate_citation_attributes(citations)
        return citations_with_attributes.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/group-citations", response_model=CitationGrouping)
async def group_citations(citations: List[CitationDimensions]):
    try:
        groups = generate_citation_groups(citations)
        return groups
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-summaries", response_model=List[CitationGroupSummary])
async def generate_summaries(groups: List[GenerateSummaryInput]):
    try:
        summaries = generate_summary_for_all_group(groups)
        return summaries.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
