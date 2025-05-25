import re


def split_js_blocks(file_path):
    """
    Split code blocks from a JavaScript file, dividing by functions, classes, or modules, and merging comments into the related code blocks.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    blocks = []
    current_block = []
    inside_block = False
    block_level = 0

    # Regular expressions for detecting function and class declarations
    function_pattern = re.compile(r'^\s*(async\s+)?function\s+[\w$]+\s*\([^)]*\)\s*(\{)?')
    arrow_function_pattern = re.compile(r'^\s*const\s+\w+\s*=\s*(async\s+)?\([^)]*\)\s*=>\s*(\{)')
    class_pattern = re.compile(r'^\s*(class|interface)\s+\w+\s*(extends\s+\w+)?\s*(implements\s+[^\{]+)?\s*(\{)?')
    module_pattern = re.compile(r'^\s*(module\.exports\s*=\s*)?{')

    # Regular expressions for detecting comments
    single_line_comment = re.compile(r'//')
    multi_line_comment_start = re.compile(r'/\*')
    multi_line_comment_end = re.compile(r'\*/')

    inside_comment_block = False
    comment_buffer = []

    lines = content.split('\n')

    for line in lines:
        stripped_line = line.strip()

        # Handle multi-line comments
        if multi_line_comment_start.search(stripped_line) and not inside_comment_block:
            inside_comment_block = True

        if inside_comment_block:
            comment_buffer.append(line)
            if multi_line_comment_end.search(stripped_line):
                inside_comment_block = False
            continue

        # Handle single-line comments
        if single_line_comment.search(stripped_line):
            comment_buffer.append(line)
            continue

        # Check if a new function, class, or module starts
        if (function_pattern.match(stripped_line) or
                arrow_function_pattern.match(stripped_line) or
                class_pattern.match(stripped_line) or
                module_pattern.match(stripped_line)):

            # Save the previous block if it exists
            if current_block:
                blocks.append('\n'.join(current_block))

            # Merge the comment buffer into the current block if it exists
            if comment_buffer:
                current_block = comment_buffer + [line]
                comment_buffer = []
            else:
                current_block = [line]

            inside_block = True
            block_level = 1
            continue

        # Check for indented lines (belonging to the current block)
        if inside_block and stripped_line and not re.match(r'^\s*$', stripped_line):
            current_block.append(line)

            # Check for opening braces, increase nesting level
            if '{' in stripped_line:
                block_level += stripped_line.count('{')

            # Check for closing braces, decrease nesting level
            if '}' in stripped_line:
                block_level -= stripped_line.count('}')

            # If nesting level is 0, the current block ends
            if block_level == 0:
                inside_block = False
                blocks.append('\n'.join(current_block))
                current_block = []
        elif not stripped_line:
            # If it's an empty line, add it to the current block
            if current_block:
                current_block.append(line)

    if current_block:
        blocks.append('\n'.join(current_block))

    # If there is a remaining comment buffer, add it as a separate block
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