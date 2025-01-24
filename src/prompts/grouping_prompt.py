import json
from typing import List
from models.regulatory_info import RegulatoryInfo


def get_grouping_prompt(citations: List[RegulatoryInfo]) -> str:
    citations_str = json.dumps([citation.model_dump() for citation in citations], indent=4)

    prompt = f""" 
You are tasked with grouping regulatory citations (including U.S. federal and state laws, as well as internal regulations) 
into Citation Groups. The grouping must follow the rules outlined below to ensure clarity, consistency, and compliance alignment.

#### Rules for Grouping:
1. **Mutual Exclusivity**:
   - Each citation must belong to only one Citation Group.
   - No citation can appear in multiple Citation Groups.

2. **Primary Grouping Criteria**:
	- Group citations primarily by **shared functional requirements** and **thematic consistency**. The goal is to create groups 
  that focus on the **core feature or requirement**, not jurisdictional differences.
	- Consider grouping based on penalties, enforcement mechanisms, or exceptions **only when they differ significantly and 
  materially affect compliance**.
   
3. **Handling Jurisdictional Differences**:
	- Combine citations across jurisdictions when the functional requirements and penalties are **reasonably similar**, 
  unless doing so would create confusion or conflict.
	
4. **Conflict Resolution**:	
	- Focus on high-level requirements over minor jurisdictional nuances.
	- Similar penalties and enforcement mechanisms should be grouped, even if they occur in different states.

--------------------------------------------

**Citations to Group**:
{citations_str}

--------------------------------------------

    """

    print(prompt.strip())

    return prompt.strip()
