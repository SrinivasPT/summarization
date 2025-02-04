from typing import List
from fastapi import FastAPI, HTTPException
from models import Citation, CitationWithAttributes, CitationGroup, CitationGroupSummary
from agents.extraction_agent.logic import generate_citation_attributes
from agents.grouping_agent.logic import generate_citation_groups
from agents.summarization_agent.logic import generate_summary_for_all_group

app = FastAPI(title="Citation Analysis API", description="API for citation extraction, grouping and summarization")


@app.post("/extract-citation-attributes", response_model=List[CitationWithAttributes])
async def extract_citations(citations: List[Citation]):
    try:
        citations_with_attributes = generate_citation_attributes(citations)
        return citations_with_attributes.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/group-citations", response_model=List[CitationGroup])
async def group_citations(citations: List[CitationWithAttributes]):
    try:
        groups = generate_citation_groups(citations)
        return groups.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-summaries", response_model=List[CitationGroupSummary])
async def generate_summaries(groups: List[CitationGroup]):
    try:
        summaries = generate_summary_for_all_group(groups)
        return summaries.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
