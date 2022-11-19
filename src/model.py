"""Model element of ccc-py(tkinter)"""
import tkinter as tk
from tkinter import ttk

import hex_to_str

start = "1.0"
end = "end"


class Model:
    """
    Attributes:
    """

    def __init__(self) -> None:
        self.text: str = ""
        self.converted_text: str = ""
        self.format_tuple = (
            "ASCII",
            "ISO-8859-1",
            "Shit_JIS",
            "UTF-8",
            "UTF-16"
        )
        self.output_format = tk.StringVar()

    def copy(self, widget: tk.Button | ttk.Button, text: str) -> None:
        widget.master.clipboard_append(text)

    def clear(self, widget: tk.Entry | tk.Text) -> None:
        if widget["state"] == "disabled":
            widget["state"] = "normal"
            widget.delete(start, end)
            widget["state"] = "disabled"
            return
        else:
            widget.delete(start, end)

    def defocus(self, event: tk.Event) -> None:
        event.widget.master.focus_set()

    def get_content(self, event: tk.Event) -> None:
        self.text = event.widget.get("1.0", "end")
        ret = ""
        match self.output_format.get():
            case "ASCII":
                ret = hex_to_str.hex_to_str(self.text, "ascii")
            case "ISO-8859-1":
                pass
            case "Shift_JIS":
                ret = hex_to_str.hex_to_str(self.text, "shift_jis")
            case "UTF-8":
                ret = hex_to_str.hex_to_str(self.text, "utf-8")
            case "UTF-16":
                ret = hex_to_str.hex_to_str(self.text, "utf-16")
            case _:
                pass

        self.converted_text = ret
