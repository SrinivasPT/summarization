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
### **Objective**
Group **all** citations dynamically based on **shared compliance requirements**, ensuring that every citation is processed. No citation should be ignored.

---

### **Instructions**
1. **Sort all citations** by restrictiveness:
   - Citations with more **key compliance requirements** are more restrictive.
   - If restrictiveness is equal, sort alphabetically by **citation number**.

2. **Group citations** based on shared compliance requirements:
   - The **most restrictive citation** starts the first group.
   - Other citations are grouped **only if** their compliance requirements match **closely** (minor wording differences should not prevent grouping).

3. **Ensure full coverage**:
   - ✅ **Every citation must appear in the output**, even if no group is found.
   - 🚨 If a citation does not match any group, it must be placed in a `"Standalone Citations"` group.
   - No citation should be ignored or omitted.

4. **Return a structured JSON response** matching this schema:
   - `group_name`: Derived from the shared compliance requirements.
   - `group_requirements`: The list of compliance obligations for this group.
   - `citations`: The citations assigned to this group.

---

### **Rules for Grouping**
✅ **Allowed:**
- A citation **must belong to exactly one group**.
- Citations can only be grouped if they **share substantively the same compliance obligations**.
- If a citation **does not fit in any group**, it **must** go into `"Standalone Citations"`.

❌ **Forbidden:**
- Ignoring or omitting citations from the output.
- Grouping citations that **do not share similar compliance obligations**.

"""

    user_message = f"""Please analyze and group the following citations using the requirement node of each citation, and according to the process described: 

{citations_str}"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
