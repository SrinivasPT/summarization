import os
import json
from typing import List

from agents.summarization_agent import process_citation_groups
from models import CitationGroup, GroupSummaryList
from utils import logger


def orchestrate_summarization(input_id: str):
    logger.log(f"Orchestrating summarization for input ID: {input_id}...")
    citation_group_list: List[CitationGroup] = read_citation_group_list(input_id)

    if citation_group_list:
        # Invoke the agent with the citation group list
        logger.log("Agent invoked with the following citation groups:")
        summaries: GroupSummaryList = process_citation_groups(citation_group_list)
        return summaries
    else:
        logger.log("No citation groups found.")
        return []


def read_citation_group_list(input_id) -> List[CitationGroup]:
    # Construct the file path
    file_path = os.path.join("data", f"{input_id}.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # Convert JSON data to CitationGroup objects
            return [CitationGroup.model_validate(item) for item in data]
    except FileNotFoundError:
        logger.log(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        logger.log(f"Error decoding JSON from file {file_path}.")
        return None
    except Exception as e:
        logger.log(f"Error processing data: {str(e)}")
        return None


if __name__ == "__main__":
    input_id = input("Enter the input ID: ")
    orchestrate_summarization(input_id)
