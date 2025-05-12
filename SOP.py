from LLM import LLMModel
from role.tester import Tester
from role.coder import Coder
from role.reviewer import Reviewer
from code_splitter.splitter_map import process_project_files
from code_splitter.rule_based import rule_based
from code_splitter.code_compressor import code_compressor

def software_development_sop(requirement, max_retries=3):
    # llm = LLMModel(model_name="glm-4-flash")
    llm = LLMModel()
    project_path = "./large_scale_project"
    output_process_file = "./code_splitter/temp/output.csv"
    output_ruled_file = "./code_splitter/temp/ruled_output.csv"
    output_compressor_file = "./code_splitter/temp/compressed_output.csv"
    process_project_files(project_path, output_process_file)
    rule_based(output_process_file, output_ruled_file)
    soft_prompt = code_compressor(output_ruled_file,output_compressor_file,llm.tokenizer,llm.model)

    developer = Coder(llm)
    tester = Tester(llm)
    reviewer = Reviewer(llm)

    retry_count = 0
    feedback = ""
    while retry_count <= max_retries:
        # 1. 开发人员开发代码
        code = developer.develop_code(requirement, soft_prompt, feedback)
        print(f"\n开发人员生成的代码:\n{code}")

        # 2. 测试人员测试
        test_result = tester.test_code(code, soft_prompt, requirement)
        print(f"\n测试人员结果: {test_result['status']}, 原因: {test_result['reason']}")

        if test_result["status"] != "采纳":
            retry_count += 1
            feedback = test_result["reason"]
            print(f"测试未通过，第 {retry_count} 次重试，反馈: {feedback}")
            continue

        # 3. Reviewer 审查
        review_result = reviewer.review_code(code, soft_prompt, requirement)
        print(f"\nReviewer 结果: {review_result['status']}, 原因: {review_result['reason']}")

        if review_result["status"] != "采纳":
            retry_count += 1
            feedback = review_result["reason"]
            print(f"审查未通过，第 {retry_count} 次重试，反馈: {feedback}")
            continue

        # 4. 流程成功
        print("\n流程成功！代码已通过测试和审查。")
        return {
            "code": code,
            "test_result": test_result,
            "review_result": review_result
        }

    # 5. 最大重试次数后失败
    print(f"\n超过最大重试次数 {max_retries}，流程失败。")
    return None