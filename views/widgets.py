from customtkinter import (
    CTkFrame,
    CTkScrollableFrame,
    CTkLabel,
    CTkToplevel,
    StringVar,
    CTkEntry,
    CTkButton,
)
from controllers.data_manager import DataManager


class ItemTable(CTkFrame):
    """
    Itemtable is a custom widget for displaying items.
    Supports editabilty but also only viewing.
    """
    def __init__(self, parent, configurable):
        super().__init__(parent)
        self.configurable = configurable # If ture enables row deletion
        self.deleted_items = set() # Tracks items for deletion

        self.item_keys = [
            "Item ID",
            "Item name",
            "On hand",
            "On order",
            "Unit value",
            "Available",
            "Total value",
            ]

        # Set up layout configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        # Frame for item header
        self.key_frame = CTkFrame(self, fg_color="#3a3b3b", height=10)
        self.key_frame.grid(row=0, column=0, sticky="nsew")

        # Scrollable frame for item rows
        self.scrollable_frame = CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        for i, key in enumerate(self.item_keys):
            self.key_frame.grid_columnconfigure(i, weight=1)
            label = CTkLabel(self.key_frame, text=key, corner_radius=10)
            label.grid(row=0, column=i, sticky="nsew")

    # Populates header labels
    def populate(self, items):
        """
        Populates the table with a list of dictonaries.

        Args:
            items (list): Linst of inventory items
        """
        # Clear Current rows
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Add each item as a row
        for i, item in enumerate(items):
            row_labels = []
            item_id = item.get("Item ID")

            for j, key in enumerate(item):
                self.scrollable_frame.grid_columnconfigure(
                    j,
                    uniform="equal",
                    weight=1,
                )
                value = item.get(key, "")
                label = CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    corner_radius=10,
                )

                # Highlight label on hover
                if self.configurable is True:
                    label.bind(
                        "<Enter>",
                        lambda e,
                        label=label: label.configure(fg_color="red"),
                    )
                    label.bind(
                        "<Leave>",
                        lambda e,
                        label=label: label.configure(fg_color="transparent"),
                    )

                label.grid(row=i, column=j, sticky="nsew")
                row_labels.append(label)

            # Double click to delete
            if self.configurable is True:
                for label in row_labels:
                    label.bind(
                        "<Button-1>",
                        lambda e,
                        item_id=item_id,
                        labels=row_labels: self.for_deletion(item_id, labels),
                    )

    def for_deletion(self, item_id, labels):
        """
        Marks item as deleted and remos from row.

        Args:
            item_id (str): id of item
            labels (list): the labels in the row
        """
        if item_id not in self.deleted_items:
            self.deleted_items.add(item_id)
            for label in labels:
                label.grid_remove()

    def get_deleted_items(self):
        """
        Returns list of ids marked for deletion
        """
        return list(self.deleted_items)


class AddPopUp(CTkToplevel):
    """
    AssPopUp gives a ui for entering a new item.
    Verifires number input and updates data manager and item table.
    """
    def __init__(self, parent, data_manager, item_table, add_button=None):
        super().__init__(parent)
        self.title("Add New Item")
        self.transient(parent) # Keep popup above parent

        self.data_manager = data_manager
        self.item_table = item_table
        self.add_button = add_button
        
        # Validation command fro numeric entry
        vcmd = (self.register(self.validate_int), '%P')

        # Initail vlaues
        self.id = self.data_manager.generate_new_id()
        self.name_var = StringVar()
        self.hand_var = StringVar()
        self.order_var = StringVar()
        self.available_var = StringVar()
        self.unit_var = StringVar()
        self.total_value_var = StringVar()
    	
        # Creates entry fields and labels
        CTkLabel(
            self,
            text=f"Item ID: {self.id}",
        ).grid(row=0, column=0, padx=10, pady=5)

        CTkLabel(
            self,
            text="Item name:",
        ).grid(row=1, column=0, padx=10, pady=5)

        CTkEntry(
            self,
            textvariable=self.name_var,
        ).grid(row=1, column=1, padx=10, pady=5)

        CTkLabel(
            self,
            text="On hand:",
        ).grid(row=2, column=0, padx=10, pady=5)

        CTkEntry(
            self,
            textvariable=self.hand_var,
            validate='key',
            validatecommand=vcmd,
        ).grid(row=2, column=1, padx=10, pady=5)

        CTkLabel(
            self,
            text="On order:",
        ).grid(row=3, column=0, padx=10, pady=5)

        CTkEntry(
            self,
            textvariable=self.order_var,
            validate='key',
            validatecommand=vcmd,
        ).grid(row=3, column=1, padx=10, pady=5)

        CTkLabel(
            self,
            text="Unit value:",
        ).grid(row=4, column=0, padx=10, pady=5)

        CTkEntry(
            self,
            textvariable=self.unit_var,
            validate='key',
            validatecommand=vcmd,
        ).grid(row=4, column=1, padx=10, pady=5)

        # Add item button
        CTkButton(
            self,
            text="Add Item",
            command=self.submit,
        ).grid(row=5, column=0, columnspan=2, pady=10)

    def submit(self):
        """
        Validates input, creates me item, updates data,
        reloads table, and closes popup
        """
        hand = int(self.hand_var.get())
        order = int(self.order_var.get())
        unit_value = int(self.unit_var.get())
        available = hand + order
        total_value = unit_value * available
        new_item = {
            "Item ID": self.id,
            "Item name": self.name_var.get(),
            "On hand": hand,
            "On order": order,
            "Unit value": unit_value,
            "Available": available,
            "Total value": total_value,
        }


        # Append to data and save
        self.data_manager.items.append(new_item)
        with open(self.data_manager.filename, "w") as f:
            import json
            json.dump(self.data_manager.items, f, indent=4)

        # Refresh table and enable add button
        self.item_table.populate(self.data_manager.items)
        self.destroy()
        self.add_button.configure(state="normal")

    def validate_int(self, new_value):
        """
        Ensures input is an interger or empty.

        Args:
            new_value (str): The value entered

        Returns:
            bool: True if valid false if not.
        """
        if new_value == "":
            return True
        return new_value.isdigit()
