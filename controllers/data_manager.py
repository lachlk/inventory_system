import json


class DataManager:
    def __init__(self, filename):

        self.filename = filename
        self.items = self.load_items()

    def load_items(self):

        with open(self.filename, 'r') as file:
            return json.load(file)

    def delete_item_by_id(self, item_ids):
        self.items = [item for item in self.items if item["Item ID"] not in item_ids]
        with open(self.filename, "w") as f:
            json.dump(self.items, f, indent=4)

    def generate_new_id(self):
        existing_ids = [item["Item ID"] for item in self.items]
        numbers = []

        for item_id in existing_ids:
            try:
                num = int(item_id)
                numbers.append(num)
            except (IndexError, ValueError):
                continue

        next_number = max(numbers, default=0) + 1
        return str(next_number)