from typing import List
from agents.extraction_agent.prompts import get_messages
from models import CitationGroup, CitationWithAttributesList
from models.llm_model import LLMModel
from utils.llm_utils import structured_llm


def generate_citation_attributes(citations: List[CitationGroup]) -> CitationWithAttributesList:
    model = LLMModel.GPT4O_MINI

    messages = get_messages(citations)

    response = structured_llm(messages=messages, response_model=CitationWithAttributesList, model=model, temperature=0.3)
    return response
