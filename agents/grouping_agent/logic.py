from typing import List
from agents.grouping_agent.prompts import get_prompt
from models import CitationGroupList, CitationWithAttributes
from utils.llm_utils import structured_llm


def generate_citation_groups(citations: List[CitationWithAttributes]) -> CitationGroupList:
    prompt = get_prompt(citations)

    # Use structured_llm to get formatted response
    response = structured_llm(prompt=prompt, response_model=CitationGroupList, model="gpt-4o-mini", temperature=0.1)

    return response
