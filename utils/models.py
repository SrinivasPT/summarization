# from enum import Enum


# class LLMModel(str, Enum):
#     # GPT Models
#     GPT4 = "gpt-4"
#     GPT35_TURBO = "gpt-3.5-turbo"
#     GPT4_TURBO = "gpt-4-turbo-preview"

#     # Ollama Models
#     LLAMA2 = "llama2"
#     LLAMA3 = "llama3.2"
#     MISTRAL = "mistral"
#     CODELLAMA = "codellama"

#     @property
#     def is_gpt(self) -> bool:
#         return self.value.startswith("gpt-")

#     @property
#     def is_ollama(self) -> bool:
#         return not self.is_gpt

#     @classmethod
#     def get_model(cls, model_name: str) -> "LLMModel":
#         try:
#             return cls(model_name.lower())
#         except ValueError:
#             valid_models = "\n".join([f"- {m.value}" for m in cls])
#             raise ValueError(f"Invalid model: {model_name}\nSupported models:\n{valid_models}")
