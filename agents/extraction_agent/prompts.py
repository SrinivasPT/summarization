from typing import List
import json
from models import CitationGroup
from pydantic import BaseModel
from utils import logger


def get_prompt(citations: List[CitationGroup]) -> str:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    prompt = f"""
Given the citations, extract regulatory information from the following text. Include detailed nuances 
such as compliance frequency, procedural requirements, and jurisdictional variations.

**Citations**:
{citations_str}


**Output**:
Respond in JSON format matching the RegulatoryInfoResponse schema.
"""
    return prompt
