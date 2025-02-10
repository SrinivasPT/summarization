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
You are an expert in regulatory compliance extraction. Your task is to dynamically extract **citation dimensions** without predefined constraints.

### **Guidelines**
1. **Identify meaningful compliance requirement dynamically** from the citation text.
2. Ensure that each requirement is **clearly defined** and **relevant**.
4. If an aspect is **not explicitly stated**, exclude it (do not return "Not Specified").
5. Ensure deterministic extraction—same input should always yield the same structured attributes.

### **Citation Data Structure**
For each citation, extract relevant compliance dimensions dynamically. The response should follow this structure:

#### Citation Entry (Example Output)
```json
{
    "citation_id": <Unique Citation ID>,
    "citation_number": "<Official Citation Number>",
    "citation_text": "<Full Text of Citation>",
    "extracted_dimensions": [
        {
            "category": "<Dynamically Determined Compliance Category>",
            "details": {
                "<Extracted Key Attribute>": "<Extracted Value>",
                "<Extracted Key Attribute>": "<Extracted Value>"
            }
        }
    ]
}
```

### **Examples of Categories (Not Predefined, Just a Reference)**
- **Regulatory Compliance**: Covers legal authorities, enforcement, and jurisdiction.
- **Financial Obligations**: Reporting, disclosure, or monetary restrictions.
- **Consumer Protection**: Transparency, fairness, and customer safeguards.
- **Technology & Data Governance**: IT security, privacy, and digital banking compliance.
- **Operational Risk**: Internal controls, record retention, or procedural mandates.
- **Market & Business Impact**: How regulations affect industry transactions or financial stability.

Extract compliance dimensions directly from the provided citations:
"""

    # User message containing citations
    user_message = f"""

{citations_str}

"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
