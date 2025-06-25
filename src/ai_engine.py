import requests
import json
from Components.config import config
from .utils.helpers import get_logger

logger = get_logger()

class AIEngine:
    def __init__(self):
        self.cache = {}
        self.timeout = 10  # seconds

    def translate(self, text, target_lang="ar"):
        if not text or not config.plugins.AIPowerFull.api_key.value:
            return "Invalid input or API key"

        # Check cache first
        cache_key = f"{target_lang}_{hash(text)}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            headers = {
                "Authorization": f"Bearer {config.plugins.AIPowerFull.api_key.value}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": f"Translate to {target_lang} accurately:"
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                "temperature": 0.3
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload),
                timeout=self.timeout
            )
            response.raise_for_status()

            result = response.json()['choices'][0]['message']['content']
            self.cache[cache_key] = result  # Cache the result
            return result

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            return f"Network Error: {str(e)}"
        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            return f"Translation Failed"
