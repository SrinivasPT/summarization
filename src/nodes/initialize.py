import json
import os
from typing import List
from models.citation import Citation
from state import State
from utils.logger import logger


def initialize(mcr_id: str) -> State:
    logger.log(f"Initializing state for MCR ID: {mcr_id}")
    # Get absolute path to data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    json_path = os.path.join(project_root, "data", f"{mcr_id}.json")

    # Load data from JSON file
    with open(json_path, "r") as file:
        data = json.load(file)

    # Create list of citations
    citations: List[Citation] = []
    for item in data:
        citation = Citation(
            rowid=item["rowid"],
            issuing_authority=item["issuing_authority"],
            citation_number=item["citation_number"],
            citation_text=item["citation_text"],
        )
        citations.append(citation)

    # Initialize state
    return State(citations=citations)
