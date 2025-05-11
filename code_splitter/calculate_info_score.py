import zlib


def calculate_info_score(code_text):
    if not code_text:
        return 0

    # 编码为字节
    code_bytes = code_text.encode('utf-8')

    # 使用 zlib 进行压缩
    compressed = zlib.compress(code_bytes)

    # 返回压缩后的字节长度作为信息量分数
    return len(compressed)