import codecs
from typing import Literal, TypeAlias

# TypeAlias encoding list
Encoding: TypeAlias = Literal["ascii", "utf-8", "utf-16", "shift_jis"]


def hex_to_str(hex_msg: str, encoding: Encoding) -> str:
    """hex_to_str

    Args:
        hex_msg (str): hexadecimal string
        encoding (Encoding): Encoding character code

    Returns:
        msg (str): Encoded string
    """
    msg = (
        codecs.decode(
            hex_msg.replace(" ", "").strip()
            .encode(errors="replace"), "hex_codec")
        .decode(encoding)
        .replace("\x00", "")
    )
    return msg
