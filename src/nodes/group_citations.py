from models.group import GroupList
from prompts.grouping_prompt import get_grouping_prompt
from state import State
from utils.llm_utils import structured_llm


def group_citations(state: State) -> State:
    """Get citation groups using LLM."""
    prompt = get_grouping_prompt(state.citations)
    group_list: GroupList = structured_llm(prompt, response_model=GroupList)

    # Convert GroupList to list of tuples (name, rowids) for state compatibility
    state.groups = [
        (group.group_name, group.citation_rowid_list) for group in group_list.group_list
    ]

    return state
