import requests
from Components.config import config
from .utils.helpers import logger

class SubtitleTranslator:
    API_URL = "https://libretranslate.de/translate"

    def translate(self, text, target_lang="ar"):
        try:
            response = requests.post(
                self.API_URL,
                json={
                    "q": text,
                    "source": "auto",
                    "target": target_lang
                },
                timeout=5
            )
            return response.json().get("translatedText", text)
        except Exception as e:
            logger().error(f"Translation API error: {e}")
            return text
