from typing import List
from models import CitationGroup, CitationGroupSummary, GroupSummaryList
from models.llm_model import LLMModel
from models.model import GenerateSummaryInput
from .prompts import get_messages
from utils import structured_llm, logger


def generate_summary_for_single_group(group: GenerateSummaryInput) -> CitationGroupSummary:
    messages = get_messages(group)

    # Use structured_llm with messages
    response = structured_llm(messages=messages, response_model=CitationGroupSummary, model=LLMModel.GPT4O_MINI, temperature=1)

    return response


def generate_summary_for_all_group(group_list: List[GenerateSummaryInput]) -> GroupSummaryList:
    logger.log("Processing citation groups...")
    summaries: List[CitationGroupSummary] = []

    # Process each group sequentially
    for group in group_list:
        summary = generate_summary_for_single_group(group)
        summaries.append(summary)

    return GroupSummaryList(data=summaries)
