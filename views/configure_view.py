from customtkinter import CTkLabel, CTkButton
from views.widgets import ItemTable
from views.base_view import BaseView

class ConfigureView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = CTkLabel(self.header_frame, text="Configure Items", font=("Roboto", 50))
        label.grid(row=1, column=0, sticky="nsw", padx=self.base_padx)

        save_button = CTkButton(self.header_frame, text="Save", font=self.base_font)
        save_button.grid(row=1, column=1, padx=self.base_padx, ipady=self.base_ipady)

        import_button = CTkButton(self.header_frame, text="Import", font=self.base_font)
        import_button.grid(row=1, column=2, padx=self.base_padx, ipady=self.base_ipady)

        add_button = CTkButton(self.control_frame, text="Add", font=self.base_font)
        add_button.grid(row=1, column=0, padx=self.base_padx, ipady=self.base_ipady)

        remove_button = CTkButton(self.control_frame, text="Remove", font=self.base_font)
        remove_button.grid(row=1, column=1, padx=self.base_padx, ipady=self.base_ipady)

        item_table = ItemTable(self.content_frame)
        item_table.grid(row=0, column=0, padx=self.base_padx, ipady=self.base_ipady)