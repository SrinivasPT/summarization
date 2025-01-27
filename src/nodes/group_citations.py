from models.citation_group import CitationGroupList, CitationGroup
from prompts.grouping_prompt import get_grouping_prompt
from state import State
from utils.llm_utils import structured_llm


def group_citations(state: State) -> State:
    """Get citation groups using LLM."""
    prompt = get_grouping_prompt(state.regulatory_info)
    group_list: CitationGroupList = structured_llm(prompt, response_model=CitationGroupList, temperature=1)
    state.groups = [(group.citation_group_name, group.citation_ids) for group in group_list.citation_group_list]

    return state
