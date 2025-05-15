from customtkinter import CTkFrame


class BaseView(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.base_font = ("Roboto", 20)
        self.base_padx = 15
        self.base_ipady = 15

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=4)

        self.header_frame = CTkFrame(self, fg_color="#3a3b3b")
        self.header_frame.grid(row=0, column=0, sticky="nsew")
        self.header_frame.grid_columnconfigure(0, weight=3)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=2)
        self.header_frame.grid_rowconfigure(2, weight=1)

        self.control_frame = CTkFrame(self)
        self.control_frame.grid(row=1, column=0, sticky="nsew")
        self.control_frame.grid_rowconfigure(0, weight=1)
        self.control_frame.grid_rowconfigure(1, weight=2)
        self.control_frame.grid_rowconfigure(2, weight=1)

        self.content_frame = CTkFrame(self)
        self.content_frame.grid(row=2, column=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
