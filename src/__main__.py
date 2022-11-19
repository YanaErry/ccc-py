import tkinter as tk

from controller import CharEncodeController, Controller
from model import Model
from views import Form, View


class Application(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master = master

        self.master.resizable(height=False, width=False)
        self.master.title('ccc-py')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.NSEW)

    def new_tab(self, controller: Controller, view: View) -> None:
        view = view(self.master)  # type: ignore
        controller.bind(view)


if __name__ == '__main__':
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    encode_controller = CharEncodeController(model=Model())
    app = Application(master=root)
    app.new_tab(view=Form, controller=encode_controller)  # type: ignore
    app.mainloop()
