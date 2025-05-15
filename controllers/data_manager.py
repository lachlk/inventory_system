import json


class DataManager:
    """
    Manages data in json file. Eg, Loadingm deleting and generating id.
    """

    def __init__(self, filename):
        """
        Sets path to json file.

        Args:
            filename: path to file
        """
        self.filename = filename
        self.items = self.load_items()

    def load_items(self):
        """
        Load items

        Returns:
            list: A list of items
        """
        with open(self.filename, 'r') as file:
            return json.load(file)

    def delete_item_by_id(self, item_ids):
        """
        Delete items that match a ID

        Args:
            item_ids: List of ids to be deleted
        """
        self.items = [item for item in self.items if item["Item ID"] not in item_ids]
        with open(self.filename, "w") as f:
            json.dump(self.items, f, indent=4)

    def generate_new_id(self):
        """
        Generates unique id as string.
        
        The id is one greater than the previous.

        Returns:
            str: the item id
        """
        existing_ids = [item["Item ID"] for item in self.items]
        numbers = []

        # Converts existing id to int and ignores invalid ids
        for item_id in existing_ids:
            try:
                num = int(item_id)
                numbers.append(num)
            except (IndexError, ValueError):
                continue
        
        # Gets next id by adding one to the largest found and defualts to one if none
        next_number = max(numbers, default=0) + 1
        return str(next_number)