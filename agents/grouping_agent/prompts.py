import json
from typing import List, Dict
from pydantic import BaseModel
from models.model import CitationWithAttributes
from openai.types.chat import ChatCompletionMessageParam


def get_messages(citations: List[CitationWithAttributes]) -> List[ChatCompletionMessageParam]:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    system_message = """
    
You are provided with a set of regulatory citations related to a common compliance obligation. These citations originate from various jurisdictions and may include jurisdiction-specific nuances or additional procedural details. Your task is to group these citations into a clear, hierarchical structure **without over-dividing the top level**.

> **Important Guidelines:**
>
> - **Core Obligation:** All citations address the same fundamental compliance requirement.
>
> - **Top-Level Grouping:**
>   - Place **all** citations addressing the core obligation into one single top-level group.
>   - Do not split the top level based on minor wording differences or variations that do not materially affect how the obligation is met.
>
> - **Subgrouping for Material Differences Only:**
>   - **Create only one level of subgroups** if there are material differences that affect how the compliance obligation is met.
>   - Material differences include additional or conditional steps (e.g., extra requirements, conditional language, or extension procedures) that materially alter the compliance process.
>   - **Do not create subgroups** based solely on minor procedural or wording differences.
>
> - **Unique Placement:**   
>   - Ensure every citation appears in **one and only one** group.

---

### **Your Task**

1. **Identify the Core Compliance Obligation:**

   - Recognize that each citation shares a fundamental compliance requirement.

2. **Group All Citations at the Top Level:**

   - Start by placing all citations in one overall group addressing the core compliance obligation.

3. **Create Subgroups Only if Needed (Material Differences):**

  Example Subgroups Structure:
   * **Subgroup 1 (Baseline Compliance):** Citations that define the core, fundamental requirement, representing the minimum necessary actions for compliance. These citations describe the standard process without any additional conditions or variations.

   * **Subgroup 2 (Variations and Additional Requirements):** Citations that introduce variations to the baseline compliance process or impose additional, materially different requirements. These variations significantly alter the actions needed to achieve compliance. Further subgrouping within this category is recommended to distinguish *different types* of variations. Examples:

      * **Subgroup 2.1 (Procedural Variations):** Citations that specify alternative procedures or steps for fulfilling the core requirement. These variations change *how* the core requirement is met (e.g., different filing methods, specific notification timelines).
            * **Subgroup 2.1.1 (Procedural Variations):** Citations that specify alternative procedures or steps for fulfilling the core requirement. These variations change *how* the core requirement is met (e.g., different filing methods, specific notification timelines).

      * **Subgroup 2.2 (Conditional Requirements):** Citations that introduce conditions that trigger additional obligations or modify the baseline requirements. These conditions can be based on specific circumstances, events, or thresholds (e.g., reporting thresholds, examination results).

      * **Subgroup 2.3 (Enhanced Requirements):** Citations that impose additional or enhanced requirements beyond the baseline. These are not simply variations on the process but represent distinct, added obligations (e.g., additional reporting, specific documentation needs).

4. **Ensure Unique Group Placement:**

   - Each citation should appear in one subgroup only.

---

Follow these guidelines to produce a grouping that accurately reflects whether additional steps materially alter the compliance process, rather than splitting the group based on minor language differences

"""

    user_message = f"""Please analyze and group the following citations according to the process described: 

{citations_str}"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
