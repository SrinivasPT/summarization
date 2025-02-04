import json
from typing import List
from pydantic import BaseModel
from models.model import CitationWithAttributes


def get_prompt(citations: List[CitationWithAttributes]) -> str:
    if not (isinstance(citations, list) and all(isinstance(c, BaseModel) for c in citations)):
        raise TypeError("Input must be a list of Citation models")

    citations_str = "\n".join([json.dumps(c.model_dump(), indent=4) for c in citations])

    prompt = f"""
You are tasked with grouping **regulatory citations** into **hierarchical Citation Groups**. Follow these steps:

---

### Step 1: Identify Top-Level Categories
Group citations into **top-level categories** based on their **core functional requirements** (e.g., "Data Confidentiality", "Fraud Prevention"). These categories represent high-level compliance domains.

---

### Step 2: Drill Down into Subgroups
For each top-level category, create **subgroups** based on:
1. **Risk Level**: High, Medium, or Low (prioritize citations with severe penalties as High Risk).
2. **Penalty Details**: Group citations with similar penalties together.
3. **Jurisdiction**: Combine citations from multiple jurisdictions if their requirements and penalties are substantially similar.
4. **Procedural Nuances**: Combine citations if they have substantially similar Procedural Nuances.
5. **Significant Nuances**: Create separate groups for citations that have **unique or significant procedural or jurisdictional nuances**, even if they share functional requirements with other citations.
6. **Unique Requirements**: Create separate groups for citations that have **unique requirements** that do not align with other citations in the same functional category.

---

### Step 3: Apply Grouping Rules
1. **Mutual Exclusivity**: Each citation belongs to only one group.
2. **Functional Alignment**: Group by shared functional requirements (e.g., "Disclosure restriction").
3. **Jurisdictional or Procedural Nuances Similarity**: Citations across jurisdictions are combined if they have similar jurisdictional applicability or procedural requirements.
4. **Significant Nuances**: Citations with significant procedural or jurisdictional nuances should be placed in their own subgroup, even if they share functional requirements with other citations.
5. **Unique Requirements**: Citations with unique requirements that do not align with other citations in the same functional category should be placed in their own subgroup.
6. Create manageable groups that **minimize overlaps** and ensure that **each group reflects distinct compliance or legal obligations**.
7. **Risk-Based Prioritization**: Group based on compliance complexity or enforcement severity.

---

### Example Hierarchical Grouping:
1. **Top-Level Category**: Data Confidentiality
   - **Subgroup 1**: High-Risk Disclosure Restrictions
     - **Risk Level**: High (due to significant penalties).
     - **Citations**: "Mass. Gen. Laws ch. 62E, §14", "Haw. Rev. Stat. § 576D-15(f)".
   - **Subgroup 2**: Moderate-Risk Disclosure Restrictions
     - **Risk Level**: Moderate (no significant penalties).
     - **Citations**: "Ky. Rev. Stat. § 131.676(1)", "Ky. Rev. Stat. § 131.676(4)".
   - **Subgroup 3**: Unique Procedural Nuances
     - **Risk Level**: Medium
     - **Citations**: "N.Y. Comp. Codes R. & Regs. tit. 2, § 123.3" (due to specific form and notarization requirements).

---

### Attributes for Grouping:
1. **Functional Requirement**: Core compliance need (e.g., "Disclosure restriction").
2. **Applicable Entity**: Who the citation applies to (e.g., "Financial institutions").
3. **Risk Level**: Severity of non-compliance (High, Medium, Low).
4. **Penalty Details**: Penalty severity (e.g., "$1,000 per violation").
5. **Jurisdiction**: Combine if requirements are similar across jurisdictions.
6. **Procedural Nuances**: Specific procedural requirements (e.g., online submission, certification, notarization).
7. **Significant Nuances**: Unique procedural or jurisdictional requirements that necessitate separate grouping.
8. **Unique Requirements**: Requirements that are distinct and do not align with other citations in the same functional category.

---

### Objective:
Create a **hierarchical structure of Citation Groups** that emphasizes **functional alignment**, **risk prioritization**, and **separation of citations with significant nuances or unique requirements** for efficient compliance management, **with out repeating citations** across different groups.

---

### Citations to Group:
{citations_str}

"""
    return prompt
