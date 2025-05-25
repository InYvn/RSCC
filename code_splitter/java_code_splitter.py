import re


def split_java_blocks(file_path):
    """
    Split code blocks from a Java file, dividing by classes and methods while preserving comments.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    blocks = []
    current_block = []
    inside_block = False
    block_level = 0

    # Regular expressions for detecting class and method declarations
    class_pattern = re.compile(r'^\s*(public|private|protected|static|final|abstract|\s)*class\s+(\w+)')
    method_pattern = re.compile(
        r'^\s*((public|private|protected|static|final|abstract|synchronized|native|strictfp|\s)+)?(\w+|\w+<.*?>|\w+\[\])\s+(\w+\s*\(*.*?\)*)')
    interface_pattern = re.compile(r'^\s*(public|private|protected|static|final|abstract|\s)*interface\s+(\w+)')

    # Regular expressions for detecting comments
    single_line_comment = re.compile(r'//')
    multi_line_comment_start = re.compile(r'/\*')
    multi_line_comment_end = re.compile(r'\*/')

    inside_comment_block = False

    for line in lines:
        stripped_line = line.strip()

        # Handle multi-line comments
        if multi_line_comment_start.search(stripped_line) and not inside_comment_block:
            inside_comment_block = True

        if inside_comment_block:
            current_block.append(line)
            if multi_line_comment_end.search(stripped_line):
                inside_comment_block = False
            continue

        # Handle single-line comments
        if single_line_comment.search(stripped_line):
            current_block.append(line)
            continue

        # Check if a new class or method starts
        if class_pattern.match(stripped_line) or interface_pattern.match(stripped_line):
            # Save the previous block if it exists
            if current_block:
                blocks.append(''.join(current_block))

            current_block = [line]
            inside_block = True
            block_level = 1
            continue

        # Check if a new method starts
        if method_pattern.match(stripped_line):
            current_block.append(line)
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
                blocks.append(''.join(current_block))
                current_block = []
        elif not stripped_line:
            # If it's an empty line, add it to the current block
            if current_block:
                current_block.append(line)

    if current_block:
        blocks.append(''.join(current_block))

    return blocks


if __name__ == "__main__":
    file_path = "example.java"
    code_blocks = split_java_blocks(file_path)

    for i, block in enumerate(code_blocks):
        print(block)
        print("-" * 50)