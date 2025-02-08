from typing import List
import json
from models import CitationGroup
from pydantic import BaseModel
from utils import logger
from openai.types.chat import ChatCompletionMessageParam


def get_messages(citations: List[CitationGroup]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """You are a regulatory information extraction system. Your task is to extract specific details from regulatory citations with high precision and consistency.

Follow these guidelines strictly:
1. Extract precisely the information requested in the Pydantic model.
2. Report the information as written in the citation, without interpretation or summarization.
3. The 'risk_level' field must match exactly one of the following values: 'LOW', 'MEDIUM', 'HIGH'.
4. If a field's information is not explicitly stated in the citation, set the field's value to null in the JSON.
5. The output must be invariable for a given citation. Aim for deterministic and reproducible results."""

    user_message = f"""Please extract regulatory information from the following citations:

{citations_str}"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
