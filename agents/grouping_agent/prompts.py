import json
from typing import List
from pydantic import BaseModel
from models.citation_dimensions import CitationDimensions
from openai.types.chat import ChatCompletionMessageParam


def get_messages(citations: List[CitationDimensions]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of CitationDimensions models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
Act as a **Regulatory Compliance Analyst** responsible for analyzing citations under a **Major Compliance Requirement (MCR)** and grouping them based on shared compliance nuances.
    
## **Objective**
- Given a set of regulatory citations under a **single Major Compliance Requirement (MCR)**, determine the **appropriate Attribute-level groupings** based on shared compliance nuances.  
- The grouping process should **begin with the most restrictive citation**, ensuring that compliance is structured around the highest regulatory standard first.  
- If a citation does not contain any qualifying nuances, it should be tagged directly under the **MCR level** without being grouped into an Attribute.

### **Nuances:** Conditions That Determine the Creation of an Attribute:
An **Attribute** must be created whenever citations share **common compliance requirements** but differ in any of the following nuances. Even **minor variations within a nuance** require the formation of a **separate Attribute**.

- **Nature of Obligation:**  
  - Defines whether compliance is **mandatory, conditional, or optional**.  
  - If two citations impose compliance differently (e.g., one mandates reporting while another makes it conditional on entity size), they must belong to **separate Attributes**.  

- **Procedural Specificity:**  
  - Specifies how compliance must be achieved, including:
    - **Required formats** (e.g., online submission vs. paper filing).  
    - **Filing deadlines or extensions** (e.g., annual vs. quarterly reporting).  
    - **Additional approvals or certifications** (e.g., notarization requirements).  
  - If any procedural step varies between citations, **a distinct Attribute must be created**.  

- **Scope of Application:**  
  - Defines which entities must comply based on criteria such as:
    - **Entity type** (e.g., financial institutions vs. general businesses).  
    - **Size thresholds** (e.g., companies with **$10M+ net worth** vs. those with **$1M+ in revenue**).  
    - **Operational history** (e.g., businesses operating for at least five years).  
  - If a citation applies to a different subset of entities, it must be placed under a **separate Attribute**.  

- **Enforcement Mechanisms:**  
  - Outlines how compliance is monitored and enforced, including:
    - **Regulatory audits and examinations** (e.g., required periodic reviews).  
    - **Penalties for non-compliance** (e.g., fines vs. license suspension).  
    - **Corrective actions** (e.g., compliance plans, reporting adjustments).  
  - If enforcement conditions differ between citations, a **new Attribute must be created**.  

---

## **Definitions**
- **Major Compliance Requirement (MCR):** A broad regulatory obligation that all associated citations relate to.
- **Attribute:** A specific compliance dimension that qualifies or refines the applicability of citations within an MCR.
- **Citations:** Legal or regulatory references that describe compliance obligations. Citations may have different nuances that dictate how compliance applies to specific entities.
- **Most Restrictive Citation:** The citation that imposes the strictest conditions within an Attribute.  

### **How Stringency is Measured**:
  - **Severity of penalties** for non-compliance.  
  - **Complexity of procedural requirements** (e.g., notarization, additional approvals).  
  - **Breadth of application** (e.g., applies to a broader range of entities).  

---

## **Instructions While Reading Citations**
1. Each citation has a **requirements node**, which contains the **list of requirements extracted from the citation**.
2. Give priority to **these extracted requirements** when grouping citations, but use citation text as well while determining grouping.

## **Expected Output Format (JSON)**
Your response **must strictly follow** this JSON format:

```json
{
  "mcr_name": "<Name of the Major Compliance Requirement>",
  "mcr_requirements": [
    "<Key compliance obligation under this MCR>",
    "<Additional compliance obligations if applicable>"
  ],
  "attributes": [
    {
      "attribute_name": "<Name of the attribute based on shared compliance nuances>",
      "attribute_requirements": [
        "<Key compliance obligations that define this attribute>"
      ],
      "citations": [
        {
          "citation_id": <Unique ID of the citation>,
          "citation_number": "<Reference number of the citation>",
          "is_mcr_level": false
        }
      ]
    }
  ],
  "mcr_level_citations": [
    {
      "citation_id": <Unique ID of the citation>,
      "citation_number": "<Reference number of the citation>",
      "is_mcr_level": true
    }
  ]
}

"""

    user_message = f"""Please analyze and group the following citations using the requirement node of each citation, and according to the process described: 

{citations_str}"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]


# 1. Each citation has requirements node, which will have the list of requirements extracted from citation. Use requirements only while grouping citations.
# 1. Each citation has citation_text node. Use citation_text alone for grouping citations.
# - Each citation has a **requirements node**, which contains the **list of requirements extracted from the citation**.
# - Give priority to **these extracted requirements** when grouping citations, but use citation text as well while determining grouping.
# - Ensure that grouping is based strictly on **shared compliance obligations** and not inferred assumptions.
# 1. Each input citation has citation_text node. Use citation_text alone for grouping citations.
