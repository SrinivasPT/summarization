from models import CitationGroup
from pydantic import BaseModel
from utils import logger


def get_prompt(group: CitationGroup) -> str:
    if not isinstance(group, BaseModel):
        raise TypeError("Input must be a Pydantic model")

    group_citations_str = group.model_dump()

    prompt = f"""
You are a legal compliance expert. Your task is to generate a detailed, legally accurate, 
and actionable compliance summary for the group "{group.citation_group_name}" based on the provided legal citations. 
This summary must fully reflect legal obligations with precision, covering all conditions, 
exceptions, and nuances necessary for regulatory compliance.

--------------------------------------------

Comprehensive Instructions for Generating the Summary
1. Start with a Clear and Enforceable Directive Obligation
Use "Edge Bank must..." or "Edge Bank must not..." to clearly state required or prohibited actions.
Always use mandatory and authoritative language to convey legal obligations.
Avoid interpretive or suggestive terms such as "should" or "may".

2. Fully Capture Conditions, Exceptions, and Limitations
Explicitly state all conditions, timeframe, or triggering events under which the requirement applies.
Include any exceptions, exemptions, or permissible deviations mentioned in the law.
Reflect any thresholds, limits, or qualifiers (e.g., financial caps, timing constraints).

3. Maintain Legal Complexity and Nuances
Ensure complex legal relationships (e.g., multiple clauses or layered conditions) are fully and 
accurately represented. Preserve detailed legal language without oversimplifying critical provisions.

4. Identify the Governing Legal Authority
Clearly state the regulatory authority enforcing the requirement (e.g., Commissioner, Department of Financial Institutions).
Specify if compliance involves reporting to, notifying, or seeking approval from that authority.

5. Highlight Legal and Financial Implications
Clearly outline any penalties, fees, liabilities, or sanctions for non-compliance.
Include any deadlines, processing times, or compliance frequency requirements when applicable.

6. Use Legally Precise and Directive Language
Reflect the exact wording and intent of the statute.
Use precise, formal, and unambiguous legal terminology.
Ensure the tone is authoritative and aligned with legal standards.

7. Accurately Cite Legal Authorities
End each summary with:
"Citation(s): [Citation Reference Codes]" for proper traceability.
Ensure all relevant statutes, codes, and sections are cited correctly.

--------------------------------------------

Formatting Requirements
1) Summary Format: "Edge Bank must/must not [specific actions] when [conditions or relevant timeframe], except [any legal exception]. Citation(s): [Citation Reference Codes]"

2) Description: Provide a brief but comprehensive explanation that fully captures the legal obligation, 
reflecting all relevant conditions and nuances without introducing operational details.

3) Citations: Include the issuing authority, citation number, and the full legal text for complete context and traceability.

--------------------------------------------

Enhanced Examples
1) For Balloon Mortgage Disclosures (Florida Law): "Edge Bank must clearly disclose when a mortgage is a 
balloon mortgage by prominently printing or stamping a legend on the first page and above the mortgagor’s signature line. 
For fixed-rate balloon mortgages, the legend must state the final principal payment or balance due at maturity. 
For variable-rate balloon mortgages, the disclosed amount must approximate the balance assuming the initial interest rate 
applies for the entire loan term, with a statement that the actual balance may vary. Citation(s): Fla. Stat. §697.05(2)."

2) For Investor Disclosures in Mortgage Loans (Arizona Law): "Before accepting funds from non-institutional investors 
for a mortgage loan, Edge Bank must provide: (1) an independent property valuation, (2) a preliminary title report 
disclosing encumbrances, and (3) a disclosure statement detailing borrower information, property conditions, mortgage terms, 
and the broker’s role. Citation(s): Ariz. Rev. Stat. §6-907(A)."

3) For Payment Processing and Legal Notices (Virgin Islands Law):
"Edge Bank must not terminate, suspend, or modify its rights or duties to pay an item or charge a customer’s account after 
receiving a legal notice, stop-payment order, or legal process, if a reasonable time for Edge Bank to act has passed. 
This restriction applies once Edge Bank has accepted, paid, certified, or become accountable for the item. 
Citation(s): 11A V.I.C. Art 4 § 4-303(a)."

--------------------------------------------

Goal
The generated summaries must be:
1. Legally precise — Reflect the exact legal obligations and wording of the citation.
2. Comprehensive — Fully capture all legal conditions, exceptions, and limitations.
3. Clear and Directive — Use formal, authoritative, and enforceable legal language.
4. Consistent — Maintain structure, tone, and clarity aligned with legal compliance standards.

By incorporating these refinements, the prompt will generate compliance summaries that are fully aligned 
with legal standards and provide a complete, accurate representation of the cited legal obligations.

--------------------------------------------
**Citations Group Name**: {group.citation_group_name}

{group_citations_str}
--------------------------------------------
    """

    logger.log(prompt.strip())

    return prompt.strip()
