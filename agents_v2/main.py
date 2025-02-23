import json
from typing import List
from models.llm_model import LLMModel
from utils import logger
from utils.llm_utils import structured_llm

from .grouping_prompt import get_citations_grouping_prompt_messages, get_categorize_citations_review_prompt_messages
from .tag_citations_prompt import get_tag_citation_prompt_messages, get_tag_citation_review_prompt_messages
from .standardization_prompt import get_standardize_citation_messages, get_standardize_citation_review_messages
from .model import Citation, CitationGroupList, CitationWithTags, StandardCitation, StandardCitationList, CitationWithTagsList


def generate_grouping(citations: List[Citation]) -> StandardCitationList:
    model = LLMModel.GPT4O
    top_p = 0.7
    temperature = 0.3

    # Standardize citation text
    messages = get_standardize_citation_messages(citations)
    standardize_response: StandardCitationList = structured_llm(
        messages=messages, response_model=StandardCitationList, model=model, temperature=temperature, top_p=top_p
    )
    print_json(standardize_response.citations)

    # # Review the Standardize citation text
    # messages = get_standardize_citation_review_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=StandardCitationList, model=model, temperature=1)
    # print_json(response.citations)

    # Tag citations with themes
    messages = get_tag_citation_prompt_messages(standardize_response.citations)
    tag_response: CitationWithTagsList = structured_llm(
        messages=messages, response_model=CitationWithTagsList, model=model, temperature=temperature, top_p=top_p
    )
    logger.log(tag_response.core_legal_obligation)
    print_json(tag_response.citations)

    # # Review Tag citations with themes
    # messages = get_tag_citation_review_prompt_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithTagsList, model=model, temperature=1)
    # print_json(response.citations)

    # Categorize citations based on core_legal_obligation and specific_compliance_details
    messages = get_citations_grouping_prompt_messages(tag_response.core_legal_obligation, tag_response.citations)
    group_response: CitationGroupList = structured_llm(
        messages=messages, response_model=CitationGroupList, model=model, temperature=temperature, top_p=top_p
    )
    logger.log(group_response.mcr_level_group)
    print_json(group_response.groups)

    # # Review citations categorization based on core_legal_obligation and specific_compliance_details
    # messages = get_categorize_citations_review_prompt_messages(response.citations)
    # response: StandardCitationList = structured_llm(messages=messages, response_model=CitationWithCategoryList, model=model, temperature=1)
    # print_json(response.citations)

    return group_response


def print_json(citations: StandardCitation | CitationWithTags):
    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])
    logger.log(citations_str)
    # print(citations_str)
