from typing import Type, List
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_fireworks import ChatFireworks
from ollama import chat
from .logger import logger
from models import LLMModel
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# Load environment variables
load_dotenv()


def handle_ollama_response(
    messages: List[ChatCompletionMessageParam], model: str, response_model: Type[BaseModel], temperature: float
) -> BaseModel:
    return response_model.model_validate_json(
        chat(
            messages=messages,
            model=model,
            format=response_model.model_json_schema(),
            options={"temperature": temperature, "num_predict": 8192},
        ).message.content
    )


def handle_fireworks_response(
    messages: List[ChatCompletionMessageParam], model: str, response_model: Type[BaseModel], temperature: float
) -> BaseModel:
    return (
        ChatFireworks(model=model, temperature=temperature, fireworks_api_key=os.getenv("FIREWORKS_API_KEY"), max_tokens=8000)
        .with_structured_output(response_model)
        .invoke(messages)
    )


def handle_gpt_response(
    messages: List[ChatCompletionMessageParam], model: str, response_model: Type[BaseModel], temperature: float
) -> BaseModel:
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=messages,
            response_format=response_model,
            temperature=temperature,
            max_tokens=8000,
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        logger.log(f"OpenAI parsing error: {str(e)}")
        raise


def structured_llm(
    messages: List[ChatCompletionMessageParam],
    response_model: Type[BaseModel],
    model: LLMModel = LLMModel.GPT4O_MINI,
    temperature: float = 1,
) -> BaseModel:
    try:
        if not 0 <= temperature <= 2:
            raise ValueError("Temperature must be between 0 and 2")

        # Log messages
        logger.log("Processing LLM request with messages:")
        for msg in messages:
            logger.log_llm_prompt(f"Role: {msg['role']}")
            logger.log_llm_prompt(f"Content: {msg['content']}...")  # Log first 500 chars to avoid too verbose logs

        handler_map = {"ollama": handle_ollama_response, "fireworks": handle_fireworks_response, "gpt": handle_gpt_response}

        model_type = next((k for k in handler_map.keys() if getattr(model, f"is_{k}")), None)
        if not model_type:
            raise ValueError(f"Unsupported model type: {model}")

        return handler_map[model_type](messages, model.value, response_model, temperature)

    except Exception as e:
        logger.log("Error occurred in structured_llm:")
        logger.log(f"Model: {model.value}")
        logger.log(f"Temperature: {temperature}")
        logger.log(f"Response Model: {response_model.__name__}")
        logger.log(f"Error: {str(e)}")
        raise
