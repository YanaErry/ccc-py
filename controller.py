from abc import ABC, abstractmethod

from model import Model
from views import Form, View

start = '1.0'
end = 'end'


class Controller(ABC):
    @abstractmethod
    def bind(self, view: View):
        raise NotImplementedError


class CharEncodeController(Controller):
    def __init__(self, model: Model) -> None:
        self.model = model
        self.view: Form

    def bind(self, view: Form):  # type: ignore[override]
        self.view = view
        self.view.create_view()
        self.bind_input_label()
        self.bind_output_label()

    def bind_input_label(self):
        self.view.comboboxes["input_format_combobox"].config(
            values=self.model.format_tuple
        )
        self.view.comboboxes["input_format_combobox"].bind(
            "<FocusIn>", self.model.defocus
        )
        self.view.texts["input_text"].bind("<Return>", self.model.defocus)

        self.view.buttons["input_clear_btn"].config(
            command=lambda: self.view.texts["input_text"].delete(start, end)
        )

    def bind_output_label(self):
        self.view.texts["output_text"].config(state="disabled")
        self.view.buttons["output_copy_btn"].config(
            command=lambda: self.view.master.clipboard_append(
                self.model.str_input_msg
            )
        )
