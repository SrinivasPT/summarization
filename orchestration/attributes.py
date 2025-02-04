import json
import os
from typing import List
from agents.extraction_agent.logic import generate_citation_attributes
from models.model import CitationGroup, CitationWithAttributesList
from utils import logger


def orchestrate_attributes_extraction(input_id: str):
    logger.log(f"Orchestrating attributes extraction for input ID: {input_id}...")
    citations: List[CitationGroup] = read_citations(input_id)
    citationAttributeList: CitationWithAttributesList = generate_citation_attributes(citations)
    return citationAttributeList


def read_citations(input_id: str) -> List[CitationGroup]:
    # Construct the file path
    file_path = os.path.join("data", f"{input_id}.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # Convert JSON data to Citation objects
            return [CitationGroup.model_validate(item) for item in data]
    except FileNotFoundError:
        logger.log(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        logger.log(f"Error decoding JSON from file {file_path}.")
        return []
    except Exception as e:
        logger.log(f"Error processing data: {str(e)}")
        return []
