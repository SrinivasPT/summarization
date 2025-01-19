import json
from typing import List
from models.citation import Citation


def get_grouping_prompt(citations: List[Citation]) -> str:

    citations_str = json.dumps(
        [citation.model_dump() for citation in citations], indent=4
    )

    prompt = f""" 
**Task**: You are a legal compliance expert. Your task is to group the 
following legal citations based on their compliance obligations. The goal 
is to mirror how a human legal expert would combine or separate them.

--------------------------------------------

**Rules for Grouping Citations**:

1. **Combine Citations with Identical or Similar Compliance Obligations**:
   - If multiple citations (even from different jurisdictions) require 
     the **same operational steps**, impose the **same penalties**, or 
     can be satisfied by **one internal compliance procedure**, group 
     them together.
   - *Example*: If two statutes both say “financial institutions must 
     not disclose to an account holder that their name was given to the 
     government” and impose the **same fines** for violations, they 
     should be combined—even if one is from Massachusetts and the other 
     is from Hawaii.

2. **Keep Separate Groups for Distinct Compliance Requirements**:
   - If citations address the **same subject matter** but reference 
     **different processes**, **penalty structures**, or **legal 
     frameworks**, they should go in separate groups.
   - *Example*: If a statute requires **additional disclosures** or 
     places **different liabilities** on the institution, it should be 
     in a separate group.

3. **Provide a Brief Explanation for Each Group**:
   - State the **common compliance function** that unites the citations 
     in that group (e.g., “non‑disclosure of taxpayer info to the 
     account holder”).
   - If you split citations, briefly explain why (e.g., “Kentucky’s 
     statutes have a different fee/penalty structure from 
     Massachusetts/Hawaii”).

4. **Ensure One Citation Appears in Only One Group**:
   - Each citation should belong to **only one group**. Do not duplicate 
     citations across groups.

--------------------------------------------

**Citations to Group**:
{citations_str}

--------------------------------------------

    """

    print(prompt.strip())

    return prompt.strip()
