import json

class JSONSpecification:
    def __init__(self):
        self.spec = {}

    def read(self, file_path: str):
        with open(file_path, 'r') as f:
            self.spec = json.load(f)
