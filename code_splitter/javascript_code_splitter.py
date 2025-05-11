import re


def split_js_blocks(file_path):
    """
    从JavaScript文件中分割代码块，按函数、类或模块分块，并将注释合并到相关代码块中
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    blocks = []
    current_block = []
    inside_block = False
    block_level = 0

    # 用于检测函数和类声明的正则表达式
    function_pattern = re.compile(r'^\s*(async\s+)?function\s+[\w$]+\s*\([^)]*\)\s*(\{)?')
    arrow_function_pattern = re.compile(r'^\s*const\s+\w+\s*=\s*(async\s+)?\([^)]*\)\s*=>\s*(\{)')
    class_pattern = re.compile(r'^\s*(class|interface)\s+\w+\s*(extends\s+\w+)?\s*(implements\s+[^\{]+)?\s*(\{)?')
    module_pattern = re.compile(r'^\s*(module\.exports\s*=\s*)?{')

    # 用于检测注释的正则表达式
    single_line_comment = re.compile(r'//')
    multi_line_comment_start = re.compile(r'/\*')
    multi_line_comment_end = re.compile(r'\*/')

    inside_comment_block = False
    comment_buffer = []

    lines = content.split('\n')

    for line in lines:
        stripped_line = line.strip()

        # 处理多行注释
        if multi_line_comment_start.search(stripped_line) and not inside_comment_block:
            inside_comment_block = True

        if inside_comment_block:
            comment_buffer.append(line)
            if multi_line_comment_end.search(stripped_line):
                inside_comment_block = False
            continue

        # 处理单行注释
        if single_line_comment.search(stripped_line):
            comment_buffer.append(line)
            continue

        # 检查是否有新的函数、类或模块开始
        if (function_pattern.match(stripped_line) or
                arrow_function_pattern.match(stripped_line) or
                class_pattern.match(stripped_line) or
                module_pattern.match(stripped_line)):

            # 如果有之前的块，保存它
            if current_block:
                blocks.append('\n'.join(current_block))

            # 如果有注释缓冲区，将其合并到当前块
            if comment_buffer:
                current_block = comment_buffer + [line]
                comment_buffer = []
            else:
                current_block = [line]

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
                blocks.append('\n'.join(current_block))
                current_block = []
        elif not stripped_line:
            # 如果是空行，添加到当前块中
            if current_block:
                current_block.append(line)

    if current_block:
        blocks.append('\n'.join(current_block))

    # 如果有剩余的注释缓冲区，将其作为单独的块
    if comment_buffer:
        blocks.append('\n'.join(comment_buffer))

    return blocks


if __name__ == "__main__":
    file_path = "example.js"
    code_blocks = split_js_blocks(file_path)

    for i, block in enumerate(code_blocks):
        print(f"Block {i + 1}:")
        print(block)
        print("-" * 50)

