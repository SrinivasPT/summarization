import json
from typing import List
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from .model import CitationWithTags, StandardCitation


def get_tag_citation_prompt_messages(citations: List[StandardCitation]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
### **Task Description:**  
You are a legal AI assistant tasked with analyzing standardized legal citations that all belong to the same **Major Compliance Requirement (MCR)** but may have jurisdiction-specific nuances. Your goal is to tag each citation with two key attributes:  

1. **Core Legal Obligations:** The fundamental legal requirement that is consistent across all jurisdictions.  
2. **Specific Compliance Details:** The jurisdiction-specific variations, exceptions, penalties, procedures, or conditions related to the citation.  

Since these citations pertain to the same MCR, ensure that the **core obligation remains consistent** across all citations while accurately reflecting jurisdiction-specific details in the compliance section.

### **Tagging Criteria:**  
- **Core Legal Obligations:** Identify the primary duty, restriction, or mandate imposed by the citation that aligns with the overarching compliance requirement.  
- **Specific Compliance Details:** Capture any jurisdictional nuances, including exceptions, penalties, liability protections, and procedural requirements.  

### **Output Format:**  
Return the citations in JSON format with two additional fields:  
- `"core_legal_obligations"`: A summary of the fundamental legal requirement that applies uniformly across all jurisdictions.  
- `"specific_compliance_details"`: A summary of specific jurisdictional conditions, exceptions, penalties, or procedural requirements.  

"""

    user_message = f"""
## **Input Citations**
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]


def get_tag_citation_review_prompt_messages(citations: List[CitationWithTags]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
### **Task Description:**  
You are a legal AI assistant tasked with reviewing and refining the tagging of standardized legal citations that pertain to the same **Major Compliance Requirement (MCR)**. Each citation has been tagged with two key attributes:  

1. **Core Legal Obligations:** The fundamental legal requirement that is consistent across all jurisdictions.  
2. **Specific Compliance Details:** Jurisdiction-specific variations, including exceptions, penalties, liability protections, procedural requirements, or other unique conditions.  

Your goal is to ensure that the tagging is accurate, consistent, and adheres to the following criteria:  

---

### **Review Criteria**  

1. **Core Legal Obligations:**  
   - Verify that the core legal obligation is consistent across all jurisdictions and accurately reflects the overarching compliance requirement.  
   - Ensure that the language used in the tagging is concise, clear, and free from jurisdiction-specific nuances.  

2. **Specific Compliance Details:**  
   - Confirm that jurisdiction-specific details are accurately captured without altering the core legal obligation.  
   - Ensure that all relevant nuances, such as exceptions, penalties, liability protections, and procedural steps, are clearly documented.  
   - Check for any missing or incomplete information in the tagging.  

3. **Consistency Across Citations:**  
   - Ensure that similar jurisdictional nuances are tagged consistently across different citations.  
   - Identify and flag any discrepancies or inconsistencies in the tagging between jurisdictions.  

4. **Legal Integrity:**  
   - Confirm that the tagging does not alter the legal meaning or intent of the original citation.  
   - Ensure that the tagging captures all material aspects of the citation, including any implicit obligations or conditions.  

---

### **Output Format**  

Return the citations in JSON format with the following updates:  
- If the tagging is accurate and complete, return the citation as-is.  
- If refinements are needed, update the `"core_legal_obligations"` and/or `"specific_compliance_details"` fields accordingly.  
- Add a new field, `"review_notes"`, to document any changes made or issues identified during the review process. 

"""

    user_message = f"""
## **Input Citations**
{citations_str}
"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
