from typing import List
from models.citation_group import CitationGroup, CitationGroupList
from prompts.summarization_prompt import get_summarization_prompt
from state import State
from models.group_summary import GroupSummary
from utils.llm_utils import structured_llm


def summarize_groups(state: State) -> State:
    """
    Summarize citations for each group in the state using an LLM.

    Args:
        state: The current pipeline state containing groups and citations
    Returns:
        Updated state with summaries for all groups
    """
    all_summaries: List[GroupSummary] = []

    # Convert tuple groups to GroupList model
    groups = CitationGroupList(
        citation_group_list=[CitationGroup(citation_group_name=name, citation_ids=citation_ids) for name, citation_ids in state.groups]
    )

    for group in groups.citation_group_list:
        citations = [c for c in state.citations if c.citation_id in group.citation_ids]

        try:
            prompt = get_summarization_prompt(group_name=group.citation_group_name, citations=citations)
            summary: GroupSummary = structured_llm(prompt, response_model=GroupSummary)
            all_summaries.extend(summary)
        except Exception as e:
            print(f"Error summarizing group {group.citation_group_name}: {str(e)}")
            continue

    state.summaries = all_summaries
    return state
