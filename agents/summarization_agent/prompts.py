from models import CitationGroup
from pydantic import BaseModel
from models.model import GenerateSummaryInput
from utils import logger
from openai.types.chat import ChatCompletionMessageParam
from typing import List


def get_messages(group: GenerateSummaryInput) -> List[ChatCompletionMessageParam]:
    if not isinstance(group, BaseModel):
        raise TypeError("Input must be a Pydantic model")

    group_citations_str = group.model_dump()

    system_message = """You are a legal compliance expert. Your task is to generate detailed, legally accurate, 
and actionable compliance summaries. Each summary must fully reflect legal obligations with precision, 
covering all conditions, exceptions, and nuances necessary for regulatory compliance.

Comprehensive Instructions for Generating the Summary:

1. Start with a Clear and Enforceable Directive Obligation
- Use "Edge Bank must..." or "Edge Bank must not..." to clearly state required or prohibited actions
- Always use mandatory and authoritative language to convey legal obligations
- Avoid interpretive or suggestive terms such as "should" or "may"

2. Fully Capture Conditions, Exceptions, and Limitations
- Explicitly state all conditions, timeframe, or triggering events
- Include any exceptions, exemptions, or permissible deviations
- Reflect any thresholds, limits, or qualifiers

3. Maintain Legal Complexity and Nuances
- Ensure complex legal relationships are fully and accurately represented
- Preserve detailed legal language without oversimplifying critical provisions

4. Use Legally Precise and Directive Language
- Reflect the exact wording and intent of the statute
- Use precise, formal, and unambiguous legal terminology
- Ensure the tone is authoritative and aligned with legal standards

5. Include Citations
- End each summary with "Citation(s): [Citation Reference Codes]" for proper traceability

Summary Format: 
"Edge Bank must/must not [specific actions] when [conditions or timeframe], except [any legal exception]. Citation(s): [Citation Reference Codes]"
"""

    user_message = f"""Please generate a compliance summary for the citation group "{group.citation_group_name}" based on these citations:

{group_citations_str}"""

    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
