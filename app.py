from customtkinter import CTkFrame
from views.stock_view import StockView
from views.configure_view import ConfigureView


class App:
    def __init__(self, root):

        self.root = root
        self.frames = {}
        self.container = CTkFrame(root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for f in (StockView, ConfigureView):
            frame = f(self.container, self)
            self.frames[f.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StockView")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
