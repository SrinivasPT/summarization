import os
from typing import Type
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def structured_llm(
    prompt: str, response_model: Type[BaseModel], model: str = "gpt-4o-mini"
) -> BaseModel:
    """
    Calls the OpenAI API and returns the response structured according to the Pydantic model.

    Args:
        prompt (str): The prompt to send to the LLM.
        response_model (Type[BaseModel]): The Pydantic model for the structured output.
        model (str): The OpenAI model to use (default: "gpt-4").

    Returns:
        BaseModel: The LLM's response parsed into the Pydantic model.
    """
    try:
        # Define the function schema for structured output
        function_schema = {
            "name": "format_response",
            "description": "Format the response according to the specified schema.",
            "parameters": response_model.model_json_schema(),
        }

        # Call OpenAI API with function calling
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            functions=[function_schema],
            function_call={"name": "format_response"},
            temperature=0,
        )

        # Extract the function arguments from the response
        function_args = response.choices[0].message.function_call.arguments

        # Parse the arguments into the Pydantic model
        return response_model.model_validate_json(function_args)
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        raise
