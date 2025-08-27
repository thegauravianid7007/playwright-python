import json
import os
from pathlib import Path
class JSONReader:
    _REPO_ROOT = Path(__file__).resolve().parent.parent
    _TESTDATA_ROOT = Path(os.getenv("TESTDATA_ROOT", _REPO_ROOT / "testdata"))
    DEFAULT_FILE = "credentials.json"

    @staticmethod
    def read_json(file_name:str = None):
        file_name = file_name or JSONReader.DEFAULT_FILE
        file_path = JSONReader._TESTDATA_ROOT / file_name
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def get_value_from_json(file_name:str, key_to_read:str):
        data = JSONReader.read_json(file_name)
        return data.get(key_to_read)
