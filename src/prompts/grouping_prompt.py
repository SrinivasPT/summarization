import json
from typing import List
from models.regulatory_info import RegulatoryInfo


def get_grouping_prompt(citations: List[RegulatoryInfo]) -> str:
    citations_str = json.dumps([citation.model_dump() for citation in citations], indent=4)

    prompt = f"""
You are tasked with grouping **regulatory citations** into **distinct Citation Groups** based on their compliance characteristics. Follow these rules:

### Step 1: Group by Core Functional Requirement
- **Group citations with similar core compliance needs** (e.g., "Negative Reporting," "Fraud Prevention").

### Step 2: General Grouping Principles
- **Mutual Exclusivity**: Each citation should belong to one group only.
- **Minimize Overlap**: Group citations that are **similar enough** but keep distinct requirements separate.
- **Risk-Based Prioritization**: Citations with higher compliance complexity or penalty risks should be placed first.

### Step 3: Separate by Key Differences
For each functional group, apply the following criteria to **separate** citations that differ:

1. **Risk Level**: Prioritize citations with higher penalties or enforcement severity as **High Risk**. Use Medium and Low Risk for less severe citations.
2. **Penalty Details**: Group citations with **similar penalties** together. Citations with vastly different penalties should be separated.
3. **Jurisdiction**: Citations from different jurisdictions may be grouped if **requirements and penalties** are closely aligned. Otherwise, separate them.
4. **Procedural Nuances**: Separate citations with **different procedural requirements** (e.g., online submission, notarization).
5. **Significant Nuances**: Separate citations with **unique jurisdictional or procedural features** (e.g., unique filing deadlines or document types).
6. **Unique Requirements**: Place citations with **distinct compliance requirements** that do not match other citations in the same functional group into their own group.

---

### Example Grouping:
**Top-Level Category**: Negative Reporting  
- **Group 1**: Medium-Risk Negative Reporting
  - Citations: "765 III. Comp. Stat. Ann. 1026/15-401(d)", "P.R. Regs. OCIF Reg. 8367 Art. 6(b)"
- **Group 2**: Unique Procedural Requirements (Notarization)
  - Citation: "N.Y. Comp. Codes R. & Regs. tit. 2, § 123.3" (Requires notarized form)
- **Group 3**: Low-Risk Negative Reporting  
  - Citations: "Ohio Admin. Code 1301:10-3-03(B)", "38 Code Miss. R. Pt. 4, R. 3.1(e)"

---

### Citations to Group:
{citations_str}

"""
    print(prompt.strip())
    return prompt.strip()
