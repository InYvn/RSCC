import re


def split_cpp_blocks(file_path):
    """
    从C++文件中分割代码块，按类和函数分块，同时保留注释
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    blocks = []
    current_block = []
    inside_block = False
    block_level = 0

    # 用于检测类和函数声明的正则表达式
    class_pattern = re.compile(r'^\s*(class|struct)\s+(\w+)')
    function_pattern = re.compile(r'^\s*((\w+\s*[\*\&]?)|\w+<.*?>|void)\s+(\w+\s*\(*.*?\)*)')

    # 用于检测注释的正则表达式
    single_line_comment = re.compile(r'//')
    multi_line_comment_start = re.compile(r'/\*')
    multi_line_comment_end = re.compile(r'\*/')

    inside_comment_block = False

    for line in lines:
        stripped_line = line.strip()

        # 处理多行注释
        if multi_line_comment_start.search(stripped_line) and not inside_comment_block:
            inside_comment_block = True

        if inside_comment_block:
            current_block.append(line)
            if multi_line_comment_end.search(stripped_line):
                inside_comment_block = False
            continue

        # 处理单行注释
        if single_line_comment.search(stripped_line):
            current_block.append(line)
            continue

        # 检查是否有新的类开始
        if class_pattern.match(stripped_line):
            # 如果有之前的块，保存它
            if current_block:
                blocks.append(''.join(current_block))

            current_block = [line]
            inside_block = True
            block_level = 1
            continue

        # 检查是否有新的函数开始
        if function_pattern.match(stripped_line):
            current_block.append(line)
            inside_block = True
            block_level = 1
            continue

        # 检查是否有缩进的代码行（属于当前块）
        if inside_block and stripped_line and not re.match(r'^\s*$', stripped_line):
            current_block.append(line)

            # 检查是否有左大括号，增加嵌套级别
            if '{' in stripped_line:
                block_level += stripped_line.count('{')

            # 检查是否有右大括号，减少嵌套级别
            if '}' in stripped_line:
                block_level -= stripped_line.count('}')

            # 如果嵌套级别为0，表示当前块结束
            if block_level == 0:
                inside_block = False
                blocks.append(''.join(current_block))
                current_block = []
        elif not stripped_line:
            # 如果是空行，添加到当前块中
            if current_block:
                current_block.append(line)

    # 如果还有未保存的块，保存它
    if current_block:
        blocks.append(''.join(current_block))

    return blocks


if __name__ == "__main__":
    file_path = "example.cpp"
    code_blocks = split_cpp_blocks(file_path)

    for i, block in enumerate(code_blocks):
        print(block)
        print("-" * 50)
