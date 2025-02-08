from typing import List
from agents.grouping_agent.prompts import get_messages
from models import CitationGroupList, CitationWithAttributes
from models.llm_model import LLMModel
from utils.llm_utils import structured_llm


def generate_citation_groups(citations: List[CitationWithAttributes]) -> CitationGroupList:
    messages = get_messages(citations)

    # Use structured_llm to get formatted response
    response = structured_llm(messages=messages, response_model=CitationGroupList, model=LLMModel.GPT4O_MINI, temperature=1)

    return response
