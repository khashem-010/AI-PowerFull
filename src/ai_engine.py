import openai
from Components.config import config

class AIEngine:
    def __init__(self):
        self.api_key = config.plugins.AIPowerFull.api_key.value

    def translate(self, text, target_lang="ar"):
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system",
                    "content": f"Translate to {target_lang} accurately:"
                },{
                    "role": "user",
                    "content": text
                }]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI Error: {str(e)}")
            return text
