from prompts.summarization_prompt import get_summarization_prompt
from state import State
from models.summary import SummaryList
from utils.llm_utils import structured_llm


def summarize_groups(state: State) -> State:
    prompt = get_summarization_prompt(state.groups, state.citations)

    llm_response = structured_llm(prompt, response_model=SummaryList)

    # Update state with summaries
    state.summaries = llm_response
    return state
