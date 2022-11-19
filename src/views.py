"""View element of ccc-py(tkinter)"""
import tkinter as tk
import tkinter.font
from abc import abstractmethod
from dataclasses import dataclass
from tkinter import ttk
from typing import Literal, TypeAlias

# TypeAlias of tk(ttk)'s widget
Button: TypeAlias = dict[str, tk.Button | ttk.Button]
Combobox: TypeAlias = dict[str, ttk.Combobox]


@dataclass
class Font:
    family: str
    size: int
    slant: Literal["italic", "roman"] = "roman"
    weight: Literal["bold", "normal"] = "normal"
    underline: bool = False
    overstrike: bool = False


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
        self.buttons: Button = dict()
        self.comboboxes: Combobox = dict()
        self.entries: dict[str, tk.Entry | ttk.Entry] = dict()
        self.frames: dict[str, ttk.Frame] = dict()
        self.labels: dict[str, ttk.Label] = dict()
        self.label_frames: dict[str, ttk.LabelFrame] = dict()
        self.texts: dict[str, tk.Text] = dict()

    def create_view(self) -> None:
        frame = tk.Frame(self.master)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky=tk.W)

        self.fontdata = Font(family="Yu Gothic UI", size=10)
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

        self.create_input_field()
        self.create_output_field()

    def create_input_field(self) -> None:
        self.create_frame(
            self.label_frames["input"],
            "input_text_frame",
            row=0,
            column=0,
            sticky=tk.NSEW,
        )
        self.create_frame(
            self.label_frames["input"],
            "input_btn_frame",
            row=1,
            column=0,
            sticky=tk.E,
        )

        self.create_text(
            self.frames["input_text_frame"],
            key="input_text",
            row=0,
            column=0,
            padx=5,
            height=12,
            fontdata=self.fontdata,
        )
        self.create_button(
            self.frames["input_btn_frame"],
            text="clear",
            key="input_clear_btn",
            row=0,
            column=0,
            pady=4,
            sticky=tk.E,
        )

    def create_output_field(self) -> None:
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
            fontdata=self.fontdata,
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
        self.labels[key] = ttk.Label(
            frame,
            text=text,
            font=self.get_font(family="Yu Gothic UI", size=10),
        )
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
        """
        LFrameStyle = ttk.Style()
        LFrameStyle.theme_use("default")
        LFrameStyle.configure("Dict.TLabelframe.Label",
        font=("Yu Gothic UI", "40", "Normal"))

        #fra_Rgst = ttk.LabelFrame(root, relief="ridge",
        # labelanchor="nw", text="LabelFrame", style="Dict.TLabelframe.Label")
        """
        self.label_frames[key] = ttk.LabelFrame(
            frame, text=label, style="Dict.TLabelframe.Label"
        )
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
        fontdata: Font,
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
        font = self.get_font(family="Yu Gothic UI", size=10)
        self.texts[key] = tk.Text(frame, height=height, width=width, font=font)
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

    def get_font(
        self,
        family: str,
        size: int,
        slant: Literal["italic", "roman"] = "roman",
        weight: Literal["bold", "normal"] = "normal",
        underline: bool = False,
        overstrike: bool = False,
    ) -> tkinter.font.Font:
        """
        if not fontdata.family:
            import os

            if os.name == "nt":
                fontdata.family = "Yu Gothic UI"
            else:
                fontdata.family = "System"
        """
        font = tkinter.font.Font(
            family=family,
            size=size,
            slant=slant,
            weight=weight,
            underline=underline,
            overstrike=overstrike,
        )
        return font
