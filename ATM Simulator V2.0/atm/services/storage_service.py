import json
import os


class StorageService:

    FILE_PATH = "data/accounts.json"

    @classmethod
    def load_data(cls):

        if not os.path.exists(cls.FILE_PATH):
            return []

        with open(cls.FILE_PATH, "r") as file:
            return json.load(file)

    @classmethod
    def save_data(cls, data):

        with open(cls.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)