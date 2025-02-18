from typing import List, Dict, Any
import json
from models import CitationGroup
from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageParam


def get_messages(citations: List[CitationGroup]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of CitationGroup Pydantic models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    # System message: Defining a flexible extraction approach
    system_message = """
# **Regulatory Compliance Requirement Extraction Prompt**

You are an **expert in regulatory compliance extraction**. Your task is to extract **fully articulated compliance requirements** dynamically from regulatory citations applicable to a large US bank.

---

## **Guidelines**
1. **Extract each individual compliance requirement as a separate list item**, ensuring clarity, completeness, and precision.
2. Each requirement must be **self-contained, fully formed, and unambiguous**, avoiding vague or partial phrases.
3. **Do not summarize multiple requirements into a single statement**—instead, **list each distinct requirement separately**.
4. If an aspect is **not explicitly mentioned**, **exclude it** (do not return "Not Specified" or make assumptions).
5. Maintain **deterministic extraction**—the same input should always yield the same structured attributes.

"""

    # User message containing citations
    user_message = f"""

{citations_str}

"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
