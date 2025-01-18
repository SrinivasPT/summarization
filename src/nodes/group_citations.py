from state import State
from models.group import Group


def group_citations(state: State) -> State:
    # Example: Call LLM to get grouping (replace with actual LLM call)
    llm_output = [
        {"group_name": "Group A", "citation_rowid_list": [1201, 1202]},
        {"group_name": "Group B", "citation_rowid_list": [1203, 1204]},
    ]

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
