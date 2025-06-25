import openai
import hashlib
import json
import os
from Components.config import config
from .utils.helpers import logger

class AIEngine:
    def __init__(self):
        self.cache_file = "/tmp/ai_powerfull_cache.json"
        self.cache = self._load_cache()

    def _load_cache(self):
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, "r") as f:
                    return json.load(f)
        except Exception as e:
            logger().error(f"Cache load error: {e}")
        return {}

    def translate(self, text, target_lang="ar"):
        if not text:
            return text
            
        cache_key = hashlib.md5(f"{target_lang}_{text}".encode()).hexdigest()
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            openai.api_key = config.plugins.AIPowerFull.api_key.value
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system",
                    "content": f"Translate to {target_lang} keeping technical terms:"
                },{
                    "role": "user",
                    "content": text
                }],
                temperature=0.3
            )
            result = response.choices[0].message.content
            self.cache[cache_key] = result
            self._save_cache()
            return result
        except Exception as e:
            logger().error(f"AI Error: {e}")
            return text

    def _save_cache(self):
        try:
            with open(self.cache_file, "w") as f:
                json.dump(self.cache, f)
        except Exception as e:
            logger().error(f"Cache save error: {e}")
