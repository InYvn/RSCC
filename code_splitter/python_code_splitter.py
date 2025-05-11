def split_code_blocks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    code_blocks = []
    current_block = []
    in_function = False
    in_class = False

    for line in lines:
        stripped_line = line.strip()

        # 检测函数定义
        if stripped_line.startswith("def "):
            if current_block:
                block_str = ''.join(current_block)
                if block_str.strip():
                    code_blocks.append(block_str)
                current_block = []
            current_block.append(line)
            in_function = True
        # 检测类定义
        elif stripped_line.startswith("class "):
            if current_block:
                block_str = ''.join(current_block)
                if block_str.strip():
                    code_blocks.append(block_str)
                current_block = []
            current_block.append(line)
            in_class = True
        else:
            # 如果在函数或类内部，继续添加到当前块
            if in_function or in_class:
                # 如果是空行，直接添加，不进行缩进判断
                if stripped_line == "":
                    current_block.append(line)
                else:
                    # 检查是否缩进回到顶部（结束当前块）
                    if not line.startswith(" " * 4):  # 假设函数/类体缩进为4个空格
                        in_function = False
                        in_class = False
                        block_str = ''.join(current_block)
                        if block_str.strip():
                            code_blocks.append(block_str)
                        current_block = []
                    current_block.append(line)
            else:
                # 模块级语句单独作为一个块
                current_block.append(line)

    # 添加最后一个块
    if current_block:
        block_str = ''.join(current_block)
        if block_str.strip():
            code_blocks.append(block_str)

    return code_blocks


def is_function_or_class_block(block):
    stripped_block = block.strip()
    return stripped_block.startswith('def ') or stripped_block.startswith('class ')


def is_comment_block(block):
    stripped_block = block.strip()
    if not stripped_block:
        return False
    # 检查是否是三引号注释
    if stripped_block.startswith('"""') and '"""' in stripped_block:
        return True
    # 或者是否是单行注释
    return stripped_block.startswith('#')


def merge_comment_blocks(code_blocks):
    merged_blocks = []
    i = 0
    while i < len(code_blocks):
        block = code_blocks[i]
        if i + 1 < len(code_blocks):
            next_block = code_blocks[i + 1]
            # 如果当前块是注释块，下一个块是函数或类块，则合并
            if is_comment_block(block) and is_function_or_class_block(next_block):
                merged_block = block + next_block
                merged_blocks.append(merged_block)
                i += 2
                continue
        merged_blocks.append(block)
        i += 1
    return merged_blocks


if __name__ == "__main__":
    file_path = "example.py"
    code_blocks = split_code_blocks(file_path)
    merged_blocks = merge_comment_blocks(code_blocks)

    for block in merged_blocks:
        print(block)
        print("-" * 50)