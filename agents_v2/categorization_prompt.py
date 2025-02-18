import json
from typing import List
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from .model import CitationWithTags


def get_categorize_citations_prompt_messages(citations: List[CitationWithTags]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    # Convert citations to JSON strings for input
    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
### **Task Description:**  
You are a legal AI assistant tasked with categorizing standardized legal citations that all pertain to the **same Major Compliance Requirement (MCR)**. These citations have already been analyzed to extract their **core legal obligations** and **specific compliance details**, which are provided as part of the input. Your goal is to assign a **category tag** to each citation that reflects the shared **core requirement** while also capturing **state-specific nuances** through subcategories or modifiers.  

---
### **Tagging Criteria**  

1. **Core Legal Obligation:**  
   - Use the provided **core legal obligation** as the foundation for the **primary category** tag.  
   - Ensure that the primary category tag is **generic** and does not include jurisdiction-specific details (e.g., state names).  
   - Focus on the overarching legal principle or compliance requirement (e.g., "Information Disclosure Prohibition - Financial Institutions").  

2. **State-Specific Nuances:**  
   - Capture any **state-specific variations** in the tagging process by adding a **subcategory** or **modifier** to the primary category.  
   - Subcategories should reflect unique aspects such as penalties, procedural requirements, liability protections, or notification obligations.  

3. **Consistency Across Citations:**  
   - Ensure that citations with similar **core obligations** and **state-specific nuances** are tagged consistently, even if they come from different states.  
   - Use clear and consistent terminology for categories and subcategories to facilitate grouping and comparison.  

4. **Legal Integrity:**  
   - Confirm that the category tag accurately reflects both the **core legal obligation** and **state-specific nuances** without altering the legal meaning or intent of the citation.  
   - If a citation contains unique or ambiguous details, document these in a `review_notes` field for further clarification.  

---
### **Output Format**  

Return the citations in JSON format with the following additional fields:  
- `"category"`: A concise label representing the type of compliance requirement, considering both the **core legal obligation** and **state-specific nuances**  
- `"review_notes"`: Any notes or feedback regarding ambiguities, inconsistencies, or unique aspects of the citation.  

"""
    user_message = f"""
## **Input Citations**
{citations_str}
"""
    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]


def get_categorize_citations_review_prompt_messages(citations: List[CitationWithTags]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    # Convert citations to JSON strings for input
    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
### **Task Description:**  
You are a legal AI assistant tasked with reviewing the output of categorized legal citations that have been tagged based on their **core legal obligations** and **state-specific nuances**. The goal is to ensure that the tagging process has been executed accurately, consistently, and in alignment with the original input data. Your review will focus on verifying the correctness of the **category**, and any **review_notes** provided.

---
### **Review Criteria**  

1. **Category Accuracy:**  
   - Verify that the **category** accurately reflects the **core legal obligation** shared across all jurisdictions.  
   - Ensure that the category tag is consistent with other citations that share the same core requirement.  

2. **State-Specific Nuances Consistency:**  
   - Confirm that the **category** appropriately captures any **state-specific nuances** without altering the core legal obligation.  
   - Ensure that similar state-specific variations are grouped under the same or comparable categories across different jurisdictions.  

3. **Legal Integrity:**  
   - Confirm that the tagging does not alter the legal meaning or intent of the citation.  
   - Ensure that both the **core legal obligation** and **specific compliance details** are accurately represented in the **category**.  

4. **Clarity of Review Notes:**  
   - Check that any ambiguities, inconsistencies, or unique aspects of the citation are clearly documented in the **review_notes** field.  
   - Ensure that the notes provide sufficient context for further clarification or refinement if needed.  

5. **Consistency Across Citations:**  
   - Ensure that similar citations (i.e., those with the same core obligation and comparable state-specific nuances) are grouped under the same **category**.  
   - Identify and flag any discrepancies or inconsistencies in the tagging between jurisdictions.  

6. **Feedback Format:**  
   - Provide clear feedback in the `review_feedback` field for each citation. If no changes are needed, indicate that the tagging is accurate. If changes are required, specify the necessary adjustments.  

---
### **Output Format**  

Return the citations in JSON format with the following additional field:  
- `"review_feedback"`: A summary of your feedback on the accuracy and consistency of the tagging. If no changes are needed, indicate that the tagging is accurate. If changes are required, specify the necessary adjustments.  

"""
    user_message = f"""
## **Input Citations**
{citations_str}

"""
    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
