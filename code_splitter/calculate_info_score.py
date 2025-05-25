import zlib


def calculate_info_score(code_text):
    if not code_text:
        return 0

    # Encode as bytes
    code_bytes = code_text.encode('utf-8')

    # Compress using zlib
    compressed = zlib.compress(code_bytes)

    # Return the length of the compressed bytes as the information score
    return len(compressed)