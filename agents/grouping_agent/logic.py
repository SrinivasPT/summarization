from typing import List
from agents.grouping_agent.prompts import get_messages
from models import CitationDimensions, MajorComplianceRequirement, LLMModel
from utils.llm_utils import structured_llm


def generate_citation_groups(citations: List[CitationDimensions]) -> MajorComplianceRequirement:
    messages = get_messages(citations)

    # Use structured_llm to get formatted response
    response = structured_llm(messages=messages, response_model=MajorComplianceRequirement, model=LLMModel.LLAMA3, temperature=0.3)

    return response
