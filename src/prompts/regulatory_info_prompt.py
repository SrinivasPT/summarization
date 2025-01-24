import json
from typing import List

from models import Citation


def get_regulatory_info_prompt(citations: List[Citation]) -> str:
    citations_str = json.dumps([citation.model_dump() for citation in citations], indent=4)

    prompt = f"""
Given the citations: generate the following details for the RegulatoryInfo class:
- Citation number
- Issuing authority
- Summary
- IsBad
- Attributes including Functional Requirement, Applicable Entity, Action Type, etc.

**Citations**:
{citations_str}


**Output**:
Respond in JSON format matching the RegulatoryInfoResponse schema.
"""
    return prompt
