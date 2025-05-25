from base_agent import Agent

class Tester(Agent):
    def __init__(self, llm_model):
        super().__init__("Tester", "Tester", llm_model)

    def test_code(self, code, soft_prompt, requirement):
        prompt = f"""
            You are a tester. Based on the following requirements and code, generate test cases and verify whether the code meets the requirements:
            Requirements: {requirement}
            Code: {code}
            Output format:
            Test cases: ...
            Test results: ...
            Failure reasons (if any): ...

            Note: The test results should use (accept/reject) and should not include both (accept/reject). Please follow the output format completely.
        """
        response = self.act(prompt, soft_prompt)

        print(response)
        # Parse the test results
        result_line = [line for line in response.splitlines() if "Test results" in line]
        if not result_line:
            return {"status": "error", "reason": "Test results not recognized"}
        result_line = result_line[0]
        disapprove = "reject" in result_line
        reason_line = [line for line in response.splitlines() if "Failure reasons" in line]
        reason = reason_line[0].replace("Failure reasons (if any): ", "") if reason_line else ""

        return {
            "status": "reject" if disapprove else "accept",
            "reason": reason
        }