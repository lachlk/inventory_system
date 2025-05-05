from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkScrollableFrame

class EntryButton:
    def __init__(self):
        self.frame = CTkFrame()
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.entry = CTkEntry(self.frame, placeholder_text="Search Items")
        self.entry.grid(row=0, column=0, sticky="nsew")

        self.button = CTkButton(self.frame, text="Enter")
        self.button.grid(row=0, column=1, sticky="nsew")

class ItemTable(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.item_keys = ["Item ID", "Item name", "On hand", "On order", "Available", "Total value"]

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.key_frame = CTkFrame(self, fg_color="#3a3b3b", height=10)
        self.key_frame.grid(row=0, column=0, sticky="nsew")

        for i, key in enumerate(self.item_keys):
            self.key_frame.grid_columnconfigure(i, weight=1)
            label = CTkLabel(self.key_frame, text=key)
            label.grid(row=0, column=i, sticky="nsew")

        self.scrollable_frame = CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        