from typing import List
from models import CitationGroup, CitationGroupSummary, GroupSummaryList
from .prompts import get_prompt
from utils import structured_llm, logger


def generate_summary_for_single_group(group: CitationGroup) -> CitationGroupSummary:
    prompt = get_prompt(group)

    # Use structured_llm to get formatted response
    response = structured_llm(prompt=prompt, response_model=CitationGroupSummary, model="gpt-4o-mini", temperature=0.1)

    # The response is already in CitationGroupSummary format
    return response


def generate_summary_for_all_group(group_list: List[CitationGroup]) -> GroupSummaryList:
    logger.log("Processing citation groups...")
    summaries: List[CitationGroupSummary] = []

    # Process each group sequentially
    for group in group_list:
        summary = generate_summary_for_single_group(group)
        summaries.append(summary)

    return GroupSummaryList(data=summaries)
