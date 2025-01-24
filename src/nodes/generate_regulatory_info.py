from models.regulatory_info import RegulatoryInfoResponse
from prompts.regulatory_info_prompt import get_regulatory_info_prompt
from state import State
from utils.llm_utils import structured_llm


def generate_regulatory_info(state: State) -> State:
    prompt = get_regulatory_info_prompt(state.citations)
    response = structured_llm(prompt, response_model=RegulatoryInfoResponse, temperature=0.2)
    state.regulatory_info = response.regulatory_info if response.regulatory_info else []
    return state
