from enum import Enum


class LLMModel(str, Enum):
    # GPT Models
    GPT4 = "gpt-4"
    GPT4O = "gpt-4o"
    GPT4O_MINI = "gpt-4o-mini"
    GPT35_TURBO = "gpt-3.5-turbo"
    GPT4_TURBO = "gpt-4-turbo-preview"

    # Ollama Models
    LLAMA2 = "llama2"
    LLAMA3 = "llama3.2"
    MISTRAL = "mistral"
    CODELLAMA = "codellama"

    # Fireworks Models
    FIREWORKS_LLAMA = "accounts/fireworks/models/llama-v2-70b"
    FIREWORKS_LLAMA3P1_8B = "accounts/fireworks/models/llama-v3p1-8b-instruct"
    FIREWORKS_MIXTRAL = "accounts/fireworks/models/mixtral-8x7b"

    @property
    def is_gpt(self) -> bool:
        return self.value.startswith("gpt-")

    @property
    def is_ollama(self) -> bool:
        return not (self.is_gpt or self.is_fireworks)

    @property
    def is_fireworks(self) -> bool:
        return self.value.startswith("accounts/fireworks/")

    @classmethod
    def get_model(cls, model_name: str) -> "LLMModel":
        try:
            return cls(model_name.lower())
        except ValueError:
            valid_models = "\n".join([f"- {m.value}" for m in cls])
            raise ValueError(f"Invalid model: {model_name}\nSupported models:\n{valid_models}")
