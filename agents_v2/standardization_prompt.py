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
## You are a legal AI assistant tasked with reviewing and standardizing legal citations for the same Major Compliance Requirement (MCR) as defined by various states or jurisdictions. The goal is to achieve uniformity in compliance language while preserving the legal integrity and jurisdiction-specific nuances of each citation. This standardization will facilitate the identification and tagging of differences between citations in later stages.

### **Review Criteria**
1. **Consistency Across Citations**
   - Ensure all citations adhere to the federal regulatory language.
   - Use standard legal terms uniformly across all citations.

2. **State-Specific Adjustments**
   - Verify that jurisdiction-specific nuances are accurately preserved

3. **Legal Integrity**
   - Confirm that modifications do not alter the legal meaning of the citations
   - Identify any missing compliance requirements.

4. **Replace the original citation_text with the standardized version using the above modifications.**.

## Provide the updated JSON as output
"""

    user_message = f"""
## **Input Citations**
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]


def get_standardize_citation_review_messages(citations: List[StandardCitation]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
## **Prompt for Reviewing and Correcting Standardized Citations**

### **Task Description:**  
You are a legal AI assistant tasked with reviewing and refining standardized legal citations to ensure compliance uniformity across multiple jurisdictions. Your goal is to verify that the citations:  
1. Maintain **consistent regulatory language** while preserving jurisdiction-specific nuances.  
2. Use **standard legal terminology** to ensure clarity and accuracy.  
3. **Do not alter the legal meaning** of any citation.  
4. Ensure that all **compliance obligations are retained** and no essential legal requirement is omitted.  
5. Correct any **inconsistencies in phrasing, structure, or formatting** while ensuring readability.  

### **Review Criteria:**  
- **Consistency Across Citations:** Verify uniformity in structure, terminology, and phrasing.  
- **State-Specific Adjustments:** Ensure jurisdiction-specific legal references remain intact.  
- **Legal Integrity:** Confirm that all obligations, restrictions, and penalties are accurately represented.  

Add a new field, `"review_notes"`, to document any changes made or issues identified during the review process.   

### **Output Format:**  
Return the corrected citations in JSON format while preserving the original citation structure.

"""

    user_message = f"""
## **Input Citations**
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
