"""View element of CharacterEncoding(tkinter)"""

import tkinter as tk
from abc import abstractmethod
from tkinter import ttk


class View(tk.Frame):
    """
    View is the base class representing the View in the MVC model
    """

    @abstractmethod
    def create_view(self):
        """Must be overridden by a subclass

        Raises:
            NotImplementedError: Not overridden by sub classes
        """
        raise NotImplementedError


class Form(View):
    """

    Args:
        View (tk.Frame): base

    Attributes:
        master (tk.Tk()): Parent widget
    """

    def __init__(self, master: tk.Frame) -> None:
        super().__init__()
        self.master = master
        self.buttons: dict[str, ttk.Button] = dict()
        self.comboboxes: dict[str, ttk.Combobox] = dict()
        self.entries: dict[str, ttk.Entry] = dict()
        self.frames: dict[str, ttk.Frame] = dict()
        self.labels: dict[str, ttk.Label] = dict()
        self.label_frames: dict[str, ttk.LabelFrame] = dict()
        self.texts: dict[str, tk.Text] = dict()

    def create_view(self) -> None:
        frame = tk.Frame(self.master)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky=tk.W)

        # input
        self.create_label_frame(
            frame,
            key="input",
            label="入力",
            row=0,
            column=0,
            padx=10,
            pady=8,
        )
        self.create_label_frame(
            frame,
            key="output",
            label="出力",
            row=1,
            column=0,
            padx=10,
            pady=8,
        )

        self.create_input_frame()
        self.create_output_frame()

    def create_input_frame(self) -> None:
        self.create_frame(
            self.label_frames["input"],
            "input_format_frame",
            row=0,
            column=0,
            sticky=tk.W,
        )
        self.create_frame(
            self.label_frames["input"],
            "input_text_frame",
            row=1,
            column=0,
            sticky=tk.NSEW,
        )
        self.create_frame(
            self.label_frames["input"],
            "input_btn_frame",
            row=2,
            column=0,
            sticky=tk.E,
        )

        self.create_label(
            self.frames["input_format_frame"],
            key="input_format_label",
            text="フォーマット",
            row=0,
            column=0,
            padx=4,
            pady=4,
            sticky=tk.EW,
        )
        self.create_combobox(
            self.frames["input_format_frame"],
            key="input_format_combobox",
            row=0,
            column=1,
            sticky=tk.EW,
        )
        self.create_text(
            self.frames["input_text_frame"],
            key="input_text",
            row=0,
            column=0,
            padx=5,
            height=12,
        )
        self.create_button(
            self.frames["input_btn_frame"],
            text="copy",
            key="input_copy_btn",
            row=0,
            column=0,
            pady=4,
            sticky=tk.E,
        )
        self.create_button(
            self.frames["input_btn_frame"],
            text="clear",
            key="input_clear_btn",
            row=0,
            column=1,
            pady=4,
            sticky=tk.E,
        )

    def create_output_frame(self) -> None:
        self.create_frame(
            self.label_frames["output"],
            "output_format_frame",
            row=0,
            column=0,
            sticky=tk.W,
        )
        self.create_frame(
            self.label_frames["output"],
            "output_text_frame",
            row=1,
            column=0,
            sticky=tk.NSEW,
        )
        self.create_frame(
            self.label_frames["output"],
            "output_btn_frame",
            row=2,
            column=0,
            sticky=tk.E,
        )

        self.create_label(
            self.frames["output_format_frame"],
            key="output_format_label",
            text="フォーマット",
            row=0,
            column=0,
            padx=4,
            pady=4,
            sticky=tk.EW,
        )
        self.create_combobox(
            self.frames["output_format_frame"],
            key="output_format_combobox",
            row=0,
            column=1,
            sticky=tk.EW,
        )
        self.create_text(
            self.frames["output_text_frame"],
            key="output_text",
            row=0,
            column=0,
            padx=5,
            height=12,
        )
        self.create_button(
            self.frames["output_btn_frame"],
            text="copy",
            key="output_copy_btn",
            row=0,
            column=0,
            pady=4,
            sticky=tk.E,
        )
        self.create_button(
            self.frames["output_btn_frame"],
            text="clear",
            key="output_clear_btn",
            row=0,
            column=1,
            pady=4,
            sticky=tk.E,
        )

    def create_combobox(
        self,
        frame,
        key,
        row,
        column,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.comboboxes[key] = ttk.Combobox(frame)
        self.comboboxes[key].grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )

    def create_button(
        self,
        frame,
        key,
        text,
        row,
        column,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.buttons[key] = ttk.Button(frame)
        self.buttons[key]["text"] = text
        self.buttons[key].grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )

    def create_entry(
        self,
        frame,
        key,
        row,
        column,
        rowspan=1,
        columnspan=1,
        width=40,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.entries[key] = ttk.Entry(frame, width=width)
        self.entries[key].grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )

    def create_frame(
        self,
        frame,
        key,
        row,
        column,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ):
        self.frames[key] = ttk.Frame(frame)
        self.frames[key].columnconfigure(column, weight=1)
        self.frames[key].rowconfigure(row, weight=1)

        self.frames[key].grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )
        return self.frames[key]

    def create_label(
        self,
        frame,
        key,
        text,
        row,
        column,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.labels[key] = ttk.Label(frame, text=text)
        self.labels[key].grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )

    def create_label_frame(
        self,
        frame,
        key,
        label,
        row,
        column,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.label_frames[key] = ttk.LabelFrame(frame, text=label)
        self.label_frames[key].grid(
            row=row,
            column=column,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )

    def create_text(
        self,
        frame,
        key,
        row,
        column,
        height=40,
        width=40,
        rowspan=1,
        columnspan=1,
        padx=0,
        pady=0,
        ipadx=0,
        ipady=0,
        sticky=tk.NSEW,
    ) -> None:
        self.texts[key] = tk.Text(frame, height=height, width=width)
        self.texts[key].grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
            ipadx=ipadx,
            ipady=ipady,
            sticky=sticky,
        )
