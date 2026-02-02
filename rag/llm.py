import os
from langchain_community.llms import Ollama
from config import LLM_MODEL


def get_llm():
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    return Ollama(
        model=LLM_MODEL,
        base_url=base_url,
        temperature=0.1
    )
