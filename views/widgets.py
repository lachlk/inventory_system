from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkScrollableFrame
from controllers.data_manager import DataManager


class EntryButton:
    def __init__(self):
        self.frame = CTkFrame()
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.entry = CTkEntry(self.frame, placeholder_text="Search Items")
        self.entry.grid(row=0, column=0, sticky="nsew")

        self.button = CTkButton(self.frame, text="Enter")
        self.button.grid(row=0, column=1, sticky="nsew")


class ItemTable(CTkFrame):
    def __init__(self, parent, configurable, data_manager):
        super().__init__(parent)
        self.configurable = configurable
        self.data_manager = data_manager

        self.item_keys = ["Item ID", "Item name", "On hand", "On order", "Available", "Total value"]

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.key_frame = CTkFrame(self, fg_color="#3a3b3b", height=10)
        self.key_frame.grid(row=0, column=0, sticky="nsew")

        self.scrollable_frame = CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        for i, key in enumerate(self.item_keys):
            self.key_frame.grid_columnconfigure(i, weight=1)
            label = CTkLabel(self.key_frame, text=key, corner_radius=10)
            label.grid(row=0, column=i, sticky="nsew")

    def populate(self, items):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, item in enumerate(items):
            row_labels = []
            item_id = item.get("Item ID")

            for j, key in enumerate(item):
                self.scrollable_frame.grid_columnconfigure(j, uniform="equal", weight=1)
                value = item.get(key, "")
                label = CTkLabel(self.scrollable_frame, text=value, corner_radius=10)

                if self.configurable == True:
                    label.bind("<Enter>", lambda e, label=label: label.configure(fg_color="red"))
                    label.bind("<Leave>", lambda e, label=label: label.configure(fg_color="transparent"))

                label.grid(row=i, column=j, sticky="nsew")
                row_labels.append(label)
                
            if self.configurable == True:
                for label in row_labels:
                    label.bind("<Button-1>", lambda e, item_id=item_id, labels=row_labels: (
                        self.data_manager.delete_item_by_id(item_id),
                        [lbl.destroy() for lbl in labels]
                    ))
