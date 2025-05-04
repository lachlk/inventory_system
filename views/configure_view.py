from customtkinter import CTkLabel, CTkButton
from views.base_view import BaseView

class ConfigureView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        base_font=("Roboto", 20)
        base_padx=15
        base_ipady=15

        label = CTkLabel(self.header_frame, text="Configure Items", font=("Roboto", 50))
        label.grid(row=1, column=0, sticky="nsw", padx=base_padx)

        save_button = CTkButton(self.header_frame, text="Save", font=base_font)
        save_button.grid(row=1, column=1, padx=base_padx, ipady=base_ipady)

        import_button = CTkButton(self.header_frame, text="Import", font=base_font)
        import_button.grid(row=1, column=2, padx=base_padx, ipady=base_ipady)

        add_button = CTkButton(self.control_frame, text="Add", font=base_font)
        add_button.grid(row=1, column=0, padx=base_padx, ipady=base_ipady)

        remove_button = CTkButton(self.control_frame, text="Remove", font=base_font)
        remove_button.grid(row=1, column=1, padx=base_padx, ipady=base_ipady)


