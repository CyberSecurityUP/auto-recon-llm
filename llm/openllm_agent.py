# llm/openllm_agent.py
import requests

class LLMReconAgent:
    def __init__(self, host="http://localhost:3000"):
        self.url = f"{host}/v1/completions"

    def generate_command(self, prompt: str) -> str:
        payload = {
            "prompt": prompt,
            "temperature": 0.2,
            "max_new_tokens": 100
        }
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            return response.json()["text"].strip()
        except Exception as e:
            return f"Error communication with OpenLLM: {e}"
