import json
import os
from pathlib import Path
class JSONReader:
    _REPO_ROOT = Path(__file__).resolve().parent.parent
    DEFAULT_FILE = Path(os.getenv("CREDENTIALS_FILE", _REPO_ROOT / "testdata" / "credentials.json"))

    @staticmethod
    def read_json(file_path:str = None):
        file_path = file_path or JSONReader.DEFAULT_FILE
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def get_value_from_json(file_path:str, key_to_read:str):
        data = JSONReader.read_json(file_path)
        return data.get(key_to_read)
