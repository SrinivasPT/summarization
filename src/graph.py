from nodes.generate_regulatory_info import generate_regulatory_info
from nodes.initialize import initialize
from nodes.group_citations import group_citations
from nodes.summarize_groups import summarize_groups
from nodes.finalize import finalize


def create_graph(mcr_id: str):
    def graph():
        # Initialize state
        state = initialize(mcr_id)

        # Generate regulatory info
        state = generate_regulatory_info(state)

        # Group citations
        state = group_citations(state)

        # Summarize groups
        # state = summarize_groups(state)

        # Prepare final output
        final_output = finalize(state)
        return final_output
        # return state

    return graph
