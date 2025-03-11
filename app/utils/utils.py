def convert_to_number(text: str) -> int:
    """
    将带有单位的数字文本（如“XX 万热度”）转换为具体的整数。

    参数:
        text (str): 输入的文本，格式为“数字 单位 热度”（如“XX 万热度”）。

    返回:
        int: 转换后的具体数字。
    """
    parts = text.split()
    number_part = parts[0]
    unit_part = parts[1]
    if unit_part == "万热度":
        return int(number_part) * 10000
    elif unit_part == "亿热度":
        return int(number_part) * 100000000
    else:
        return int(number_part)
