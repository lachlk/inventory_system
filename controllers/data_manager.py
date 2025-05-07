import json

class DataManager:
    def __init__(self, filename):
        self.filename = filename
        self.items = self.load_items()

    def load_items(self):
        with open(self.filename, 'r') as file:
            return json.load(file)
        
