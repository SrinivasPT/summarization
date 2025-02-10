from openai import OpenAI
from typing import List, Dict, Any
from pydantic import BaseModel


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    client = OpenAI()

    try:
        response = client.embeddings.create(model="text-embedding-ada-002", input=texts)
        # Extract embeddings from response
        embeddings = [item.embedding for item in response.data]
        return embeddings

    except Exception as e:
        print(f"Error generating embeddings: {str(e)}")
        return []


def generate_embeddings_for_objects(objects: List[Any], field_name: str) -> List[List[float]]:
    try:
        # Extract the specified field from each object
        texts = [getattr(obj, field_name) for obj in objects]
        return generate_embeddings(texts)
    except AttributeError as e:
        print(f"Error: Field '{field_name}' not found in object")
        return []
    except Exception as e:
        print(f"Error generating embeddings: {str(e)}")
        return []


def get_field_value(obj, field_name):
    value = obj.get(field_name)
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def add_embeddings_to_objects(objects: List[Dict], field_name: str) -> List[Dict]:
    try:
        # Extract the specified field from each object
        texts = [get_field_value(obj, field_name) for obj in objects]
        embeddings = generate_embeddings(texts)

        # Add embeddings to objects
        for obj, embedding in zip(objects, embeddings):
            obj["embedding"] = embedding

        return objects
    except Exception as e:
        print(f"Error processing embeddings: {str(e)}")
        return []
