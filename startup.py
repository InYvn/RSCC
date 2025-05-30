import argparse
from SOP import software_development_sop

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the 2048 game application generator.")
    parser.add_argument("--user_requirement", type=str, default="Create a web-based application for the 2048 game",
                        help="Specify the user requirement for the application.")
    args = parser.parse_args()

    user_requirement = args.user_requirement
    result = software_development_sop(user_requirement)

    if result:
        print("\nFinal Output:")
        print("Code:")
        print(result["code"])
        print("\nTest Results:")
        print(result["test_result"])
        print("\nReview Results:")
        print(result["review_result"])