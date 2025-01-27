import json
from typing import List

from models import Citation


def get_regulatory_info_prompt(citations: List[Citation]) -> str:
    citations_str = json.dumps([citation.model_dump() for citation in citations], indent=4)

    prompt = f"""
Given the citations, extract regulatory information from the following text. Include detailed nuances 
such as compliance frequency, procedural requirements, and jurisdictional variations.

**Citations**:
{citations_str}


**Output**:
Respond in JSON format matching the RegulatoryInfoResponse schema.
"""
    return prompt
