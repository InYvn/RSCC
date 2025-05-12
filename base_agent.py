class Agent:
    def __init__(self, name, role, llm_model):
        self.name = name
        self.role = role
        self.llm = llm_model
        self.memory = []

    def observe(self, message):
        """观察环境信息"""
        self.memory.append(f"[{self.role}] 观察到: {message}")

    def think(self, prompt, soft_prompt):
        """调用 LLM 进行思考"""
        return self.llm.generate_with_softprompt(prompt, soft_prompt)

    def act(self, action_prompt, soft_prompt):
        """执行动作（调用 LLM 并返回结果）"""
        response = self.think(action_prompt, soft_prompt)
        self.observe(f"执行动作: {action_prompt}")
        self.observe(f"响应: {response}")
        return response

    def get_memory(self):
        """获取记忆"""
        return "\n".join(self.memory)