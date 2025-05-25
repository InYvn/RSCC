def split_code_blocks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    code_blocks = []
    current_block = []
    in_function = False
    in_class = False

    for line in lines:
        stripped_line = line.strip()

        # Detect function definitions
        if stripped_line.startswith("def "):
            if current_block:
                block_str = ''.join(current_block)
                if block_str.strip():
                    code_blocks.append(block_str)
                current_block = []
            current_block.append(line)
            in_function = True
        # Detect class definitions
        elif stripped_line.startswith("class "):
            if current_block:
                block_str = ''.join(current_block)
                if block_str.strip():
                    code_blocks.append(block_str)
                current_block = []
            current_block.append(line)
            in_class = True
        else:
            # If inside a function or class, continue adding to the current block
            if in_function or in_class:
                # If it's an empty line, add it directly without checking indentation
                if stripped_line == "":
                    current_block.append(line)
                else:
                    # Check if indentation returns to the top level (end of the current block)
                    if not line.startswith(" " * 4):  # Assuming function/class body is indented by 4 spaces
                        in_function = False
                        in_class = False
                        block_str = ''.join(current_block)
                        if block_str.strip():
                            code_blocks.append(block_str)
                        current_block = []
                    current_block.append(line)
            else:
                # Module-level statements are treated as separate blocks
                current_block.append(line)

    # Add the last block
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
    # Check if it's a triple-quoted comment
    if stripped_block.startswith('"""') and '"""' in stripped_block:
        return True
    # Or if it's a single-line comment
    return stripped_block.startswith('#')


def merge_comment_blocks(code_blocks):
    merged_blocks = []
    i = 0
    while i < len(code_blocks):
        block = code_blocks[i]
        if i + 1 < len(code_blocks):
            next_block = code_blocks[i + 1]
            # If the current block is a comment block and the next block is a function or class block, merge them
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