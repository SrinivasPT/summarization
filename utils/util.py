import tiktoken

from models.llm_model import LLMModel


def get_token_size(prompt_string: str, model: LLMModel) -> int:
    encoding = tiktoken.encoding_for_model(model.value)
    tokens = encoding.encode(prompt_string)
    return len(tokens)
