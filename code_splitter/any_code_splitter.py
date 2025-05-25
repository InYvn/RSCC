import os
from code_splitter.cpp_code_splitter import split_cpp_blocks
from code_splitter.java_code_splitter import split_java_blocks
from code_splitter.javascript_code_splitter import split_js_blocks
from code_splitter.python_code_splitter import split_code_blocks
# from code_splitter.python_code_analysis import parse_function_info
# # from code_analysis.cpp_code_analysis import parse_cpp_file


def parse_file(file_path):
    # Get the file extension
    _, ext = os.path.splitext(file_path)

    if ext == '.java':
        return split_java_blocks(file_path)
    elif ext == '.py':
        return split_code_blocks(file_path)
    elif ext == '.cpp':
        return split_cpp_blocks(file_path)
    elif ext == '.js':
        return split_js_blocks(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    file_path = "./example/example.py"
    code_blocks = parse_file(file_path)

    for i, block in enumerate(code_blocks):
        print(f"Block {i + 1}:")
        print(block)
        print("-" * 50)