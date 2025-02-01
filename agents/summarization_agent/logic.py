from typing import List
from models import CitationGroup, CitationGroupSummary, GroupSummaryList
from .prompts import get_prompt
from utils import structured_llm, logger


def process_single_group(group: CitationGroup) -> CitationGroupSummary:
    prompt = get_prompt(group)

    # Use structured_llm to get formatted response
    response = structured_llm(prompt=prompt, response_model=CitationGroupSummary, model="gpt-4o-mini", temperature=0.1)

    # The response is already in CitationGroupSummary format
    return response


def process_citation_groups(group_list: List[CitationGroup]) -> GroupSummaryList:
    logger.log("Processing citation groups...")
    summaries: List[CitationGroupSummary] = []

    # Process each group sequentially
    for group in group_list:
        summary = process_single_group(group)
        summaries.append(summary)

    return GroupSummaryList(summaries=summaries)
