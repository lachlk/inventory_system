import json


class DataManager:
    def __init__(self, filename):

        self.filename = filename
        self.items = self.load_items()

    def load_items(self):

        with open(self.filename, 'r') as file:
            return json.load(file)

    def delete_item_by_id(self, item_id):
        self.items = [item for item in self.items if item["Item ID"] != item_id]
        with open(self.filename, "w") as f:
            json.dump(self.items, f, indent=4)
        print(f"Deleted item with id {item_id}")
        self.load_items()
