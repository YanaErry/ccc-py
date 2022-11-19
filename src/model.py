import tkinter as tk


class Model:
    def __init__(self) -> None:
        self._input_msg = tk.StringVar()
        self.format_tuple = ("ISO-8859-1", "Shit_JIS")

    @property
    def input_msg(self) -> tk.StringVar:
        return self._input_msg

    @property
    def str_input_msg(self) -> str:
        return self._input_msg.get()

    def copy(self) -> None:
        pass

    def defocus(self, event: tk.Event) -> None:
        event.widget.master.focus_set()
