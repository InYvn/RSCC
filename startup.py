from SOP import software_development_sop

if __name__ == "__main__":
    user_requirement = "创建一个 2048 游戏的网页版应用"
    result = software_development_sop(user_requirement)

    if result:
        print("\n最终输出:")
        print("代码:")
        print(result["code"])
        print("\n测试结果:")
        print(result["test_result"])
        print("\n审查结果:")
        print(result["review_result"])