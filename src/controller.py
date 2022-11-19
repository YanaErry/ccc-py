"""Controller element of ccc-py(tkinter)"""

import binascii
import tkinter as tk
from abc import ABC, abstractmethod

from model import Model
from views import Form, View

start = "1.0"
end = "end"


class Controller(ABC):
    """
    Controller is the base class representing the Controller in the MVC model
    """

    @abstractmethod
    def bind(self, view: View):
        """Must be overridden by a subclass

        Raises:
            NotImplementedError: Not overridden by sub classes
        """
        raise NotImplementedError


class CharEncodeController(Controller):
    def __init__(self, model: Model) -> None:
        self.model = model
        self.view: Form

    def bind(self, view: Form):  # type: ignore[override]
        self.view = view
        self.view.create_view()
        self.bind_input_field()
        self.bind_output_field()

    def bind_input_field(self):
        # bind "input_text"
        self.view.texts["input_text"].bind(
            "<KeyRelease>", self.keyrelease_input_text
        )

        # bind "input_clear_btn"
        self.view.buttons["input_clear_btn"].config(
            command=self.input_clear_btn
        )

    def bind_output_field(self):
        # bind "output_format_combobox"
        self.view.comboboxes["output_format_combobox"].config(
            values=self.model.format_tuple,
            textvariable=self.model.output_format,
        )
        self.view.comboboxes["output_format_combobox"].current(0)
        self.view.comboboxes["output_format_combobox"].bind(
            "<FocusIn>", self.model.defocus
        )

        # bind "output_text"
        self.view.texts["output_text"].config(state="disabled")

        # bind "output_copy_btn"
        self.view.buttons["output_copy_btn"].config(
            command=self.output_copy_btn
        )

    def keyrelease_input_text(self, event: tk.Event):
        widget = self.view.texts["output_text"]
        try:
            self.model.get_content(event)
        except binascii.Error:
            pass
        widget["state"] = "normal"
        widget.delete(start, end)
        widget.insert(start, self.model.converted_text)
        widget["state"] = "disabled"

    def input_clear_btn(self):
        # delete "input_text" and variable
        self.model.clear(self.view.texts["input_text"])
        self.model.text = ""
        # delete "output_text" and variable
        self.model.clear(self.view.texts["output_text"])
        self.model.converted_text = ""

    def output_copy_btn(self):
        self.model.copy(
            self.view.buttons["output_copy_btn"], self.model.converted_text
        )
