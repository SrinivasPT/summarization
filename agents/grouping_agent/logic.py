from typing import List
from agents.grouping_agent.prompts import get_messages
from models import CitationDimensions, CitationGrouping, LLMModel
from utils.llm_utils import structured_llm


def generate_citation_groups(citations: List[CitationDimensions]) -> CitationGrouping:
    messages = get_messages(citations)

    # Use structured_llm to get formatted response
    response = structured_llm(messages=messages, response_model=CitationGrouping, model=LLMModel.GPT4O_MINI, temperature=0.2)

    return response
