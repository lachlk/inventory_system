from customtkinter import *

class BaseView(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        self.header_frame = CTkFrame(self)
        self.header_frame.grid(row=0, column=0, sticky="nsew")
        self.header_frame.grid_columnconfigure(0, weight=2)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

        self.control_frame = CTkFrame(self)
        self.control_frame.grid(row=1, column=0, sticky="nsew")

        self.content_frame = CTkFrame(self)
        self.content_frame.grid(row=2, column=0, sticky="nsew")