import json
from typing import List
from models.citation import Citation
from prompts.grouping_prompt import get_grouping_prompt
from state import State
from models.group import Group, GroupList
from utils.llm_utils import call_llm, structured_llm


def group_citations(state: State) -> State:

    # Call LLM
    llm_output = llm(state.citations)

    # Create groups and update citations with group IDs
    groups = []
    for group_data in llm_output:
        group = Group(**group_data)
        groups.append(group)

        # Update citations with group_id
        for rowid in group.citation_rowid_list:
            citation = next(c for c in state.citations if c.rowid == rowid)
            citation.group_id = group.group_name

    # Update state with groups
    state.groups = groups
    return state


def llm(citations: List[Citation]) -> List[Group]:
    """
    Calls the OpenAI API with the given citations and returns the groups.

    Args:
        citations (List[Citation]): The list of citations to group.

    Returns:
        List[Group]: The list of groups.
    """
    prompt = get_grouping_prompt(citations)
    llm_response = structured_llm(prompt, response_model=GroupList)

    # Parse the LLM response (assuming it returns valid JSON)
    try:
        llm_output = json.loads(llm_response)
        # Example: Call LLM to get grouping (replace with actual LLM call)
        llm_output = [
            {"group_name": "Group A", "citation_rowid_list": [1201, 1202]},
            {"group_name": "Group B", "citation_rowid_list": [1203, 1204]},
        ]
    except json.JSONDecodeError as e:
        print(f"Error parsing LLM response: {e}")
        raise

    return llm_output
