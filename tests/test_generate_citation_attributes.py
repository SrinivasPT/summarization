import json
import os
from typing import List
import pytest
from agents.extraction_agent.logic import generate_citation_attributes
from models.model import Citation, CitationWithAttributesList
from utils import logger


# Constants
TEST_DATA_DIR = "data"
TEST_GROUP_ID = "EDGE1004440"


@pytest.fixture
def get_input_data() -> List[Citation]:
    """Fixture to load test citations from file."""
    file_path = os.path.join(TEST_DATA_DIR, f"{TEST_GROUP_ID}.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        return [Citation.model_validate(item) for item in data]


def test_generate_citation_attributes(get_input_data):
    """Test the main citation attribute generation logic."""
    # Given
    assert get_input_data, "Citation list should not be empty"

    # When
    enhanced_citation_list = generate_citation_attributes(get_input_data)

    # Then
    logger.log(f"Summaries: {enhanced_citation_list}")
    assert isinstance(enhanced_citation_list, CitationWithAttributesList)
    assert len(enhanced_citation_list.data) == len(get_input_data)
    for citation in enhanced_citation_list.data:
        assert citation.functional_requirement
        assert citation.jurisdiction
