import requests
from Components.config import config

class AIEngine:
    def translate(self, text, target_lang="ar"):
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.plugins.AIPowerFull.api_key.value}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{
                        "role": "system",
                        "content": f"Translate to {target_lang}:"
                    },{
                        "role": "user",
                        "content": text
                    }]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"
