from state import State
from utils.logger import logger


def finalize(state: State) -> dict:
    logger.log(state.model_dump())
    return state
