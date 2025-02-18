import json
from typing import List
from models.llm_model import LLMModel
from utils import logger
from utils.llm_utils import structured_llm

from .categorization_prompt import get_categorize_citations_prompt_messages, get_categorize_citations_review_prompt_messages
from .tag_citations_prompt import get_tag_citation_prompt_messages, get_tag_citation_review_prompt_messages
from .standardization_prompt import get_standardize_citation_messages, get_standardize_citation_review_messages
from .model import Citation, CitationWithCategoryList, CitationWithTags, StandardCitation, StandardCitationList, CitationWithTagsList


def generate_grouping(citations: List[Citation]) -> StandardCitationList:
    model = LLMModel.GPT4O

    # Standardize citation text
    messages = get_standardize_citation_messages(citations)
    response: StandardCitationList = structured_llm(messages=messages, response_model=StandardCitationList, model=model, temperature=1)
    print_json(response.citations)

    # # Review the Standardize citation text
    # messages = get_standardize_citation_review_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=StandardCitationList, model=model, temperature=1)
    # print_json(response.citations)

    # Tag citations with themes
    messages = get_tag_citation_prompt_messages(response.citations)
    response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithTagsList, model=model, temperature=1)
    print_json(response.citations)

    # # Review Tag citations with themes
    # messages = get_tag_citation_review_prompt_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithTagsList, model=model, temperature=1)
    # print_json(response.citations)

    # Categorize citations based on core_legal_obligation and specific_compliance_details
    messages = get_categorize_citations_prompt_messages(response.citations)
    response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithCategoryList, model=model, temperature=1)
    print_json(response.citations)

    # # Review citations categorization based on core_legal_obligation and specific_compliance_details
    # messages = get_categorize_citations_review_prompt_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithCategoryList, model=model, temperature=1)
    # print_json(response.citations)

    return response


def print_json(citations: StandardCitation | CitationWithTags):
    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])
    logger.log(citations_str)
    # print(citations_str)
