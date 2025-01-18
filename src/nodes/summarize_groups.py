from state import State
from models.summary import Summary


def summarize_groups(state: State) -> State:
    summaries = []

    for group in state.groups:
        # Example: Call LLM to generate summary (replace with actual LLM call)
        llm_output = {
            "group_id": group.group_name,
            "group_summary": f"Summary for {group.group_name}",
            "state_list": ["state1", "state2"],  # Example additional state
        }

        # Create summary and add to state
        summary = Summary(**llm_output)
        summaries.append(summary)

    # Update state with summaries
    state.summaries = summaries
    return state
