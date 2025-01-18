from typing import List
from models.group import Group
from models.citation import Citation


def get_summarization_prompt(group: Group, citations: List[Citation]) -> str:
    """
    Generates a prompt for summarizing a group of citations.

    Args:
        group (Group): The group to summarize.
        citations (List[Citation]): List of Citation objects in the group.

    Returns:
        str: Formatted prompt for the LLM.
    """
    citations_input = "\n".join(
        f"Citation {c.rowid}: {c.citation_text}"
        for c in citations
        if c.rowid in group.citation_rowid_list
    )

    prompt = f"""
    You are an expert in summarizing legal documents. Your task is to summarize the following group of citations.

    Group Name: {group.group_name}
    Citations:
    {citations_input}

    Instructions:
    1. Read the citation texts carefully.
    2. Write a concise summary that captures the main theme or topic of the group.
    3. Return the summary in the following JSON format:
        {{
            "group_id": "{group.group_name}",
            "group_summary": "Summary of the group...",
            "state_list": ["state1", "state2"]
        }}
    """
    return prompt.strip()
