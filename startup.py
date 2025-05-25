from SOP import software_development_sop

if __name__ == "__main__":
    user_requirement = "Create a web-based application for the 2048 game"
    result = software_development_sop(user_requirement)

    if result:
        print("\nFinal Output:")
        print("Code:")
        print(result["code"])
        print("\nTest Results:")
        print(result["test_result"])
        print("\nReview Results:")
        print(result["review_result"])