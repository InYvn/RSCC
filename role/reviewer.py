from base_agent import Agent


class Reviewer(Agent):
    def __init__(self, llm_model):
        super().__init__("Reviewer", "Reviewer", llm_model)

    def review_code(self, code, soft_prompt, requirement):
        prompt = f"""
            You are a code reviewer. Based on the following requirements and code, check the code's quality, compliance, and readability:
            Requirements: {requirement}
            Code: {code}
            Output format:
            Review comments: ...
            Review result: ...
            Failure reasons (if any): ...

            Note: The review result should use (accept/reject) and should not include both (accept/reject). Please follow the output format completely.
        """
        response = self.act(prompt, soft_prompt)

        print(response)
        # Parse the review result
        result_line = [line for line in response.splitlines() if "Review result" in line]
        if not result_line:
            return {"status": "error", "reason": "Review result not recognized"}
        result_line = result_line[0]
        disapprove = "reject" in result_line
        reason_line = [line for line in response.splitlines() if "Failure reasons" in line]
        reason = reason_line[0].replace("Failure reasons (if any): ", "") if reason_line else ""

        return {
            "status": "reject" if disapprove else "accept",
            "reason": reason
        }