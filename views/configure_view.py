from customtkinter import CTkLabel, CTkButton
from views.base_view import BaseView

class ConfigureView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = CTkLabel(self.header_frame, text="Configure Items")
        label.grid(row=0, column=0, columnspan=3, sticky="w")

        save_button = CTkButton(self.header_frame, text="Save")
        save_button.grid(row=0, column=1, sticky="e")

        import_button = CTkButton(self.header_frame, text="Import")
        import_button.grid(row=0, column=2, sticky="e")

        add_button = CTkButton(self.control_frame, text="Add")
        add_button.grid(row=0, column=0, sticky="nsew")

        remove_button = CTkButton(self.control_frame, text="Remove")
        remove_button.grid(row=0, column=1, sticky="nsew")


