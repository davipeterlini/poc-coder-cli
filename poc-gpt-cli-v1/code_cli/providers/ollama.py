from code_cli.providers.base import BaseProvider
import requests

class OllamaProvider(BaseProvider):
    def chat(self, messages):
        endpoint = self.config['endpoint']
        model = self.config['model']
        payload = {"model": model, "messages": messages}
        response = requests.post(f"{endpoint}/api/chat", json=payload)
        return response.json()
