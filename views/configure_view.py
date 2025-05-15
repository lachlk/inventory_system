from customtkinter import CTkLabel, CTkButton
from views.widgets import ItemTable
from views.base_view import BaseView
from controllers.data_manager import DataManager
from views.widgets import AddPopUp


class ConfigureView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.controller = controller

        self.data_manager = DataManager('data/items.json')

        self.label = CTkLabel(
            self.header_frame,
            text="Configure Items",
            font=("Roboto", 50),
        )
        self.label.grid(
            row=1,
            column=0,
            sticky="nsw",
            padx=self.base_padx,
        )

        self.save_button = CTkButton(
            self.header_frame,
            text="Save",
            font=self.base_font,
            command=self.save,
        )
        self.save_button.grid(
            row=1,
            column=1,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        self.import_button = CTkButton(
            self.header_frame,
            text="Import",
            font=self.base_font,
            state="disabled"
        )
        self.import_button.grid(
            row=1,
            column=2,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        self.add_button = CTkButton(
            self.control_frame,
            text="Add",
            font=self.base_font,
            command=self.open_pop_up
        )
        self.add_button.grid(
            row=1,
            column=0,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        self.item_table = ItemTable(self.content_frame, configurable=True)
        self.item_table.grid(
            row=0,
            column=0,
            ipady=self.base_ipady,
            sticky="nsew",
            )
        self.item_table.populate(self.data_manager.items)

    def save(self):
        deleted_ids = self.item_table.get_deleted_items()
        if deleted_ids:
            self.data_manager.delete_item_by_id(deleted_ids)
        self.item_table.deleted_items.clear()
        self.controller.show_frame("StockView")
        stock_view = self.controller.frames["StockView"]
        stock_view.data_manager.items = stock_view.data_manager.load_items()
        stock_view.item_table.populate(stock_view.data_manager.items)

    def open_pop_up(self):
        self.add_button.configure(state="disabled")
        AddPopUp(
            self,
            self.data_manager,
            self.item_table,
            add_button=self.add_button,
        )
