import json
import os
from typing import List
from agents_v2.generate_grouping import generate_grouping
from agents_v2.model import Citation


def get_input_data() -> List[Citation]:
    file_path = os.path.join("data", f"EDGE1004440.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        return [Citation.model_validate(item) for item in data]


if __name__ == "__main__":
    citations = get_input_data()
    result = generate_grouping(citations)
