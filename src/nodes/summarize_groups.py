from typing import List
from models.group import Group, GroupList
from prompts.summarization_prompt import get_summarization_prompt
from state import State
from models.summary import GroupSummary
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
    groups = GroupList(
        group_list=[
            Group(group_name=name, citation_rowid_list=rowids)
            for name, rowids in state.groups
        ]
    )

    for group in groups.group_list:
        citations = [c for c in state.citations if c.rowid in group.citation_rowid_list]

        try:
            prompt = get_summarization_prompt(
                group_name=group.group_name, citations=citations
            )
            summary: GroupSummary = structured_llm(prompt, response_model=GroupSummary)
            all_summaries.extend(summary)
        except Exception as e:
            print(f"Error summarizing group {group.group_name}: {str(e)}")
            continue

    state.summaries = all_summaries
    return state
