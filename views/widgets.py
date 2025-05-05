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
        self.grid(row=0, column=0, sticky="nsew")

        keys = "Item ID, Item name, On hand, On order, Available, Total value"

        columns = 0
        for i, key in enumerate(keys):
            label = CTkLabel(self, text=key)
            label.grid(row=0, column=i, sticky="nsew")
            columns += 1

        self.scrollable_frame = CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        self.content_frame = CTkFrame(self.scrollable_frame)
        self.content_frame.grid(row=0, column=columns, sticky="nsew")