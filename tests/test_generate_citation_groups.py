import json
import os
from typing import List
import pytest
from agents.grouping_agent.logic import generate_citation_groups
from models.model import CitationGroupList, CitationWithAttributes
from utils import logger


# Constants
TEST_DATA_DIR = "data"
TEST_GROUP_ID = "EDGE1004440_ATTR"


@pytest.fixture
def get_input_data() -> List[CitationWithAttributes]:
    """Fixture to load test citations from file."""
    file_path = os.path.join(TEST_DATA_DIR, f"{TEST_GROUP_ID}.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        return [CitationWithAttributes.model_validate(item) for item in data]


def test_generate_citation_groups(get_input_data):
    """Test the main citation attribute generation logic."""
    # Given
    assert get_input_data, "Citation list should not be empty"

    # When
    citations_with_attributes = generate_citation_groups(get_input_data)

    # Then
    logger.log(f"Summaries: {citations_with_attributes}")
    assert isinstance(citations_with_attributes, CitationGroupList)
    assert len(citations_with_attributes.data) == len(get_input_data)
    for citation in citations_with_attributes.data:
        assert citation.citation_group_id
        assert citation.citation_group_name
