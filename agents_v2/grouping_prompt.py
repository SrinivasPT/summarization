import json
from typing import List
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from .model import CitationWithTags


def get_citations_grouping_prompt_messages(mcr_core_obligation: str, citations: List[CitationWithTags]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    # Convert citations to JSON strings for input
    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = f"""
### **Task Description:**  
You are a legal AI assistant responsible for analyzing a set of standardized legal citations related to the same **Major Compliance Requirement (MCR)**:

**" {mcr_core_obligation} "**  

Your task is to **group these citations** based on whether they **match the stated MCR requirement** or have **material differences** that introduce additional nuances. Citations with **similar handling requirements** should be categorized together.

---

### **Grouping Criteria:**  
Each citation must be placed into **one** of the following categories:

1. **MCR Level Group:**  
   - Includes citations with **no material differences** from the stated MCR.  
   - There should be **no additional nuances** related to product, entity type, jurisdiction, timing, reporting methods, or any other variations beyond the core MCR requirement.  
   - These citations can be handled by a **single, shared control**.

2. **Distinct Groups for Material Differences:**  
   - Citations with **significant variations** requiring different handling must be placed in **their own groups**.  
   - Material differences can include, but are not limited to:  
     - **Product-specific requirements** (e.g., safe deposit boxes, securities)  
     - **Entity-specific conditions** (e.g., thresholds based on size or type)  
     - **Jurisdictional laws or procedural variations**  
	 - and others
   - Each distinct group should have a **clear and descriptive name** reflecting the primary difference.  
   - **Do not merge citations** into the same group unless they share the **same handling logic**.

---

### **Instructions for Grouping:**  

✅ **Step 1:**  
Identify citations that **match the MCR requirement** with **no additional nuances**.  
➡️ Place these citations under the **MCR Level Group**.

✅ **Step 2:**  
For citations with **any material differences**, create a **separate group for each unique handling requirement**.

✅ **Step 3:**  
Assign a **clear and descriptive group name** indicating the nature of the difference (e.g., "Illinois Reporting Threshold Requirements", "Jurisdiction-Specific Form Submission", "Voluntary Reporting Variations").

✅ **Step 4:**  
Provide a **justification** for why each citation belongs in its group.

✅ **Step 5 (Optional):**  
If multiple citations share **identical nuances**, you may place them in the **same group** with an explanation.

---
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
