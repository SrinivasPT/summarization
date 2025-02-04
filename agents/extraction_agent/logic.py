from typing import List
from agents.extraction_agent.prompts import get_prompt
from models import CitationGroup, CitationWithAttributesList
from utils.llm_utils import structured_llm


def generate_citation_attributes(citations: List[CitationGroup]) -> CitationWithAttributesList:
    prompt = get_prompt(citations)

    # Use structured_llm to get formatted response
    response = structured_llm(prompt=prompt, response_model=CitationWithAttributesList, model="gpt-4o-mini", temperature=0.1)

    return response
