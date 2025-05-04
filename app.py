from customtkinter import CTkFrame
from views.configure_view import ConfigureView

class App:
    def __init__(self, root):
        self.root = root

        self.container = CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)

        self.page = ConfigureView(self.container, self)
        self.page.tkraise()