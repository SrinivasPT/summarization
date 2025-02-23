import json
from typing import List
from openai.types.chat import ChatCompletionMessageParam

from pydantic import BaseModel

from .model import Citation, StandardCitation


def get_standardize_citation_messages(citations: List[Citation]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
## You are a legal AI assistant specializing in legal citation standardization across multiple jurisdictions.

## **Task**
For the given legal citation:
1. **Standardize the citation_text using consistent *federal regulatory language*, ensuring by:**
   - Standardizing legal terms as per *federal regulatory language*.
   - Removal of unnecessary statutory references (e.g., section numbers, formatting inconsistencies) unless legally essential.
   - Use of plain regulatory language while retaining proper nouns, jurisdiction names, and essential legal concepts.
   - Uniform reporting structure aligned with federal guidelines.
2. **Replace the citation_text with the standardized version using the above modifications.**.

## Provide the updated JSON as output
"""

    user_message = f"""
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]


def get_standardize_citation_review_messages(citations: List[StandardCitation]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
## You are a legal AI assistant reviewing standardized legal citations for compliance uniformity.

### **Review Criteria**
1. **Consistency Across Citations**
   - Ensure all citations adhere to the federal regulatory language.
   - Check that standard legal terms are used uniformly.
   - As all the citations belong to the same Major Compliance Requirement (MCR), but coming from various states, bring consistency across the citations with out losing / changing the compliance obligation or requirement.

2. **State-Specific Adjustments**
   - Verify that jurisdiction-specific nuances are included correctly.
   - Ensure variations are accurately represented in `state_specific_notes`.

3. **Legal Integrity**
   - Confirm that modifications do **not alter** the legal meaning.
   - Identify missing compliance requirements.

## **Output Format**
Return the citations with their updated `citation_text` field while preserving the original citation structure.
"""

    user_message = f"""
## **Citations to Review**
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
