from customtkinter import CTkLabel, CTkButton
from views.widgets import ItemTable
from views.base_view import BaseView
from controllers.data_manager import DataManager


class StockView(BaseView):
    """
    StockView extends baseview to display data only.
    Some buttons are palce holders for future function.
    """
    def __init__(self, parent, controller):
        """
        Initalises the layout, headerm controls, table.

        Args:
            parent: parent container.
            controller: for navigating views.
        """
        super().__init__(parent, controller)

        self.controller = controller

        # load data from file
        self.data_manager = DataManager('data/items.json')

        # Display title in header
        self.label = CTkLabel(
            self.header_frame,
            text="Stock Report",
            font=("Roboto", 50),
        )
        self.label.grid(
            row=1,
            column=0,
            sticky="nsw",
            padx=self.base_padx,
        )

        # Place holder
        self.order_button = CTkButton(
            self.header_frame,
            text="Order Items",
            font=self.base_font,
            state="disabled",
        )
        self.order_button.grid(
            row=1,
            column=1,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        self.create_button = CTkButton(
            self.header_frame,
            text="Create Invoice",
            font=self.base_font,
            state="disabled",
        )
        self.create_button.grid(
            row=1,
            column=2,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        # Button for switching to configure view
        self.configure_button = CTkButton(
            self.control_frame,
            text="Configure Items",
            font=self.base_font,
            command=lambda: self.controller.show_frame("ConfigureView"),
        )
        self.configure_button.grid(
            row=1,
            column=0,
            padx=self.base_padx,
            ipady=self.base_ipady,
        )

        # Table to only display items
        self.item_table = ItemTable(self.content_frame, configurable=False)
        self.item_table.grid(
            row=0,
            column=0,
            ipady=self.base_ipady,
            sticky="nsew",
        )

        # Populate table with items
        self.item_table.populate(self.data_manager.items)
