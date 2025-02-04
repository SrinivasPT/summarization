import json
import os
from typing import List
import pytest
from agents.summarization_agent.logic import generate_summary_for_all_group
from models.model import CitationGroup, GroupSummaryList
from utils import logger


# Constants
TEST_DATA_DIR = "data"
TEST_GROUP_ID = "EDGE1004440_GROUP"


@pytest.fixture
def get_input_data() -> List[CitationGroup]:
    """Fixture to load test citation groups from file."""
    file_path = os.path.join(TEST_DATA_DIR, f"{TEST_GROUP_ID}.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        return [CitationGroup.model_validate(item) for item in data]


def test_process_citation_groups(get_input_data):
    """Test the main summarization processing logic."""
    # Given
    assert get_input_data, "Citation group list should not be empty"

    # When
    summaries = generate_summary_for_all_group(get_input_data)

    # Then
    logger.log(f"Summaries: {summaries}")
    assert isinstance(summaries, GroupSummaryList)
    assert len(summaries.data) == len(get_input_data)
    for summary in summaries.data:
        assert summary.citation_group_summary
        assert summary.citation_group_id
