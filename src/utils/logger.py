import logging
from pathlib import Path

# Basic config for root logger
logging.basicConfig(level=logging.INFO)


class Logger:
    def __init__(self):
        self.log_dir = Path(__file__).parent.parent.parent / "logs"
        self.log_dir.mkdir(exist_ok=True)

        # Setup llm logger
        self.llm_logger = logging.getLogger("llm_logger")
        self.llm_logger.setLevel(logging.INFO)
        self.llm_logger.propagate = False  # Prevent duplicate logging

        # Add file handler with UTF-8 encoding
        llm_handler = logging.FileHandler(self.log_dir / "llm.log", encoding="utf-8")
        llm_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.llm_logger.addHandler(llm_handler)

        # Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.llm_logger.addHandler(console_handler)

        # Setup response logger
        self.app_logger = logging.getLogger("logger")
        self.app_logger.setLevel(logging.INFO)
        self.app_logger.propagate = False

        # Add file handler with UTF-8 encoding
        app_handler = logging.FileHandler(
            self.log_dir / "application.log", encoding="utf-8"
        )
        app_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.app_logger.addHandler(app_handler)

        # Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.app_logger.addHandler(console_handler)

    def log_llm_prompt(self, value: str):
        """Log a prompt to the prompts.log file"""
        separator = "=" * 80
        self.llm_logger.info(f"\n{separator}\nPROMPT\n{separator}\n{value}\n\n")

    def log_llm_response(self, value: str):
        """Log a prompt to the prompts.log file"""
        separator = "=" * 80
        self.llm_logger.info(f"\n{separator}\nRESPONSE\n{separator}\n{value}\n\n")

    def log(self, message: str):
        """Log a response to the responses.log file"""
        self.app_logger.info(f"\n{message}\n")


# Create a singleton instance
logger = Logger()
