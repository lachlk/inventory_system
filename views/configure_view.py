from customtkinter import CTkLabel, CTkButton
from views.widgets import ItemTable
from views.base_view import BaseView
from controllers.data_manager import DataManager

class ConfigureView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.data_manager = DataManager('data/items.json')

        self.label = CTkLabel(self.header_frame, text="Configure Items", font=("Roboto", 50))
        self.label.grid(row=1, column=0, sticky="nsw", padx=self.base_padx)

        self.save_button = CTkButton(self.header_frame, text="Save", font=self.base_font)
        self.save_button.grid(row=1, column=1, padx=self.base_padx, ipady=self.base_ipady)

        self.import_button = CTkButton(self.header_frame, text="Import", font=self.base_font)
        self.import_button.grid(row=1, column=2, padx=self.base_padx, ipady=self.base_ipady)

        self.add_button = CTkButton(self.control_frame, text="Add", font=self.base_font)
        self.add_button.grid(row=1, column=0, padx=self.base_padx, ipady=self.base_ipady)

        self.remove_button = CTkButton(self.control_frame, text="Remove", font=self.base_font)
        self.remove_button.grid(row=1, column=1, padx=self.base_padx, ipady=self.base_ipady)

        self.item_table = ItemTable(self.content_frame)
        self.item_table.grid(row=0, column=0, ipady=self.base_ipady, sticky="nsew")
        self.item_table.populate(self.data_manager.items)