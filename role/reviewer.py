from base_agent import Agent

class Reviewer(Agent):
    def __init__(self, llm_model):
        super().__init__("Reviewer", "Reviewer", llm_model)

    def review_code(self, code, soft_prompt, requirement):
        prompt = f"""
            你是一个代码审查员。根据以下需求和代码，检查代码质量、规范性和可读性：
            需求: {requirement}
            代码: {code}
            输出格式：
            审查意见: ...
            审查结果: ...
            失败原因（如存在）: ...
            
            注意事项：审查结果使用（采纳/不通过）表示，请勿同时出现（采纳/不通过）。请按照输出格式完整输出。
        """
        response = self.act(prompt, soft_prompt)

        print(response)
        # 解析审查结果
        result_line = [line for line in response.splitlines() if "审查结果" in line]
        if not result_line:
            return {"status": "error", "reason": "审查结果未识别"}
        result_line = result_line[0]
        disapprove = "不通过" in result_line
        reason_line = [line for line in response.splitlines() if "失败原因" in line]
        reason = reason_line[0].replace("失败原因（如存在）: ", "") if reason_line else ""

        return {
            "status": "不通过" if disapprove else "采纳",
            "reason": reason
        }