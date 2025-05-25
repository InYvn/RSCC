class Agent:
    def __init__(self, name, role, llm_model):
        self.name = name
        self.role = role
        self.llm = llm_model
        self.memory = []

    def observe(self, message):
        """Observe environmental information"""
        self.memory.append(f"[{self.role}] Observed: {message}")

    def think(self, prompt, soft_prompt):
        """Invoke the LLM to think"""
        return self.llm.generate_with_softprompt(prompt, soft_prompt)

    def act(self, action_prompt, soft_prompt):
        """Perform an action (invoke the LLM and return the result)"""
        response = self.think(action_prompt, soft_prompt)
        self.observe(f"Performed action: {action_prompt}")
        self.observe(f"Response: {response}")
        return response

    def get_memory(self):
        """Retrieve memory"""
        return "\n".join(self.memory)