from state import State


def finalize(state: State) -> dict:
    # Example: Prepare final output as a dictionary
    final_output = {
        "citations": [c.dict() for c in state.citations],
        "groups": [g.dict() for g in state.groups],
        "summaries": [s.dict() for s in state.summaries],
    }
    return final_output
