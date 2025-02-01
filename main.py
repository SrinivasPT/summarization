from typing import Optional
import sys

from orchestration.summarization import orchestrate_summarization
from utils import logger


def main(input_id: str, operation: Optional[str] = ""):
    logger.log(f"Starting main with Input ID: {input_id}, Operation: {operation}")
    try:
        if operation.lower() == "summarization":
            logger.log("Performing summarization operation...")
            result = orchestrate_summarization(input_id)
            return result

        return []  # Return empty list for unknown operations

    except Exception as e:
        logger.log(f"Error occurred: {str(e)}")
        return []


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        logger.log("Usage: python main.py <input_id> [operation]")
        sys.exit(1)

    input_id = sys.argv[1]
    operation = sys.argv[2] if len(sys.argv) == 3 else ""

    result = main(input_id, operation)
    logger.log(result)
