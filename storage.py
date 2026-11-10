import json
from pathlib import Path
from platformdirs import user_data_path

class Storage:
    def __init__(self):
        self.data_dir = user_data_path('InventorySystem')
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.file_path = self.data_dir / 'inventory.json'

        if not self.file_path.exists():
            self.save({})

    def load(self):
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    def save(self, data):
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def clear(self):
        self.save({})