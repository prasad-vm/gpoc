import yaml

class YamlTemplate:
    def __init__(self):
        self.template = {}

    def read(self, file_path: str):
        with open(file_path, 'r') as f:
            self.template = yaml.safe_load(f)

    def update(self, spec: dict):
        for key, value in spec.items():
            self.template[key] = value

    def write(self, file_path: str):
        with open(file_path, 'w') as f:
            yaml.dump(self.template, f)