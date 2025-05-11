from zhipuai import ZhipuAI
import os

class LLMModel:
    def __init__(self, model_name="glm-4-flash-250414", api_key=""):
        self.model_name = model_name
        self.api_key = api_key if api_key else os.getenv("ZHIPUAI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key 未设置，请提供有效的 ZhipuAI API Key")

        self.client = ZhipuAI(api_key=self.api_key)

    def generate(self, prompt, system_prompt=""):
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages
        )

        return response.choices[0].message.content.strip()