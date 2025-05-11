from base_agent import Agent

class Coder(Agent):
    def __init__(self, llm_model):
        super().__init__("开发人员", "开发人员", llm_model)

    def develop_code(self, requirement, feedback=None):
        base_prompt = f"""
            你是一个开发人员。根据以下需求开发代码：
            {requirement}
            输出格式：
            代码文件结构: ...
            核心代码实现: ...
        """
        if feedback:
            base_prompt += f"\n请根据以下反馈进行改进：{feedback}"

        return self.act(base_prompt)