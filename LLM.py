from zhipuai import ZhipuAI
import os
from compressor.support_compression_LLM import generate_with_softprompt, initialize_model

class LLMModel:
    def __init__(self):
        """Initialize the model and tokenizer"""
        self.tokenizer, self.model = initialize_model()

    def generate_with_softprompt(self, prompt_text, soft_prompt):
        """Generate text with a soft prompt"""
        return generate_with_softprompt(self.tokenizer, self.model, prompt_text, soft_prompt)