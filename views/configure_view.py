from customtkinter import CTkLabel, CTkButton
from views.widgets import ItemTable
from views.base_view import BaseView
from controllers.data_manager import DataManager
from views.widgets import AddPopUp


class ConfigureView(BaseView):
    """
    Configure view inherits/extends BaseView for the interface for viewing and interating.
    Including adding and deleting items to persistant storage.
    """
    def __init__(self, parent, controller):
        """
        Initalises ui and data.

        Args:
            parent: Parent container
            controller: used for navigating views
        """
        super().__init__(parent, controller)

        self.controller = controller

        # Load data form json file
        self.data_manager = DataManager('data/items.json')

        # Create header title
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

        # Button for saving changes
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

        # Button to add data in a popup
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

        # Item table with ability to delete items
        self.item_table = ItemTable(self.content_frame, configurable=True)
        self.item_table.grid(
            row=0,
            column=0,
            ipady=self.base_ipady,
            sticky="nsew",
            )
        self.item_table.populate(self.data_manager.items)

    def save(self):
        """
        Save the inventory. And deleted items are removed from the json file, updating stockview.
        """
        deleted_ids = self.item_table.get_deleted_items()
        if deleted_ids:
            self.data_manager.delete_item_by_id(deleted_ids)

        # Clears the list of deleted items
        self.item_table.deleted_items.clear()

        # Switch to StockView and refresh its table
        self.controller.show_frame("StockView")
        stock_view = self.controller.frames["StockView"]
        stock_view.data_manager.items = stock_view.data_manager.load_items()
        stock_view.item_table.populate(stock_view.data_manager.items)

    def open_pop_up(self):
        """
        Disables the add button till the popup is gone.
        And creates a popup for adding items
        """
        self.add_button.configure(state="disabled")
        AddPopUp(
            self,
            self.data_manager,
            self.item_table,
            add_button=self.add_button,
        )
