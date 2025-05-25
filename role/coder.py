from base_agent import Agent

class Coder(Agent):
    def __init__(self, llm_model):
        super().__init__("Developer", "Developer", llm_model)

    def develop_code(self, requirement, soft_prompt, feedback=None):
        base_prompt = f"""
            You are a developer. Develop code based on the following requirements:
            {requirement}
            Output format:
            Code file structure: ...
            Core code implementation: ...
        """
        if feedback:
            base_prompt += f"\nPlease make improvements based on the following feedback: {feedback}"

        return self.act(base_prompt, soft_prompt)