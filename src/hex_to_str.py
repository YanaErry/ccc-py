import codecs


def hex_to_str(hex_msg: str) -> str:
    """hex_to_str

    Args:
        hex_msg (str): hexadecimal string

    Returns:
        msg(str): string(utf-8)
    """
    msg = codecs.decode(hex_msg.encode("latin-1"), "hex_codec").decode("utf-8")
    return msg
