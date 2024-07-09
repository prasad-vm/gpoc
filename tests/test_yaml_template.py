import unittest
from io import StringIO
import yaml
from src.yaml_template import YamlTemplate

class TestYamlTemplate(unittest.TestCase):
    def test_read(self):
        yaml_data = "key1: value1\nkey2: value2\n"
        yaml_file = StringIO(yaml_data)

        yaml_template = YamlTemplate()
        yaml_template.read(yaml_file)

        self.assertEqual(yaml_template.template, {"key1": "value1", "key2": "value2"})

    def test_update(self):
        yaml_data = "key1: value1\nkey2: value2\n"
        yaml_file = StringIO(yaml_data)

        yaml_template = YamlTemplate()
        yaml_template.read(yaml_file)
        yaml_template.update({"key2": "new_value2", "key3": "value3"})

        self.assertEqual(yaml_template.template, {"key1": "value1", "key2": "new_value2", "key3": "value3"})

    def test_write(self):
        yaml_template = YamlTemplate()
        yaml_template.template = {"key1": "value1", "key2": "value2"}

        output = StringIO()
        yaml_template.write(output)

        self.assertEqual(output.getvalue(), "key1: value1\nkey2: value2\n")

if __name__ == "__main__":
    unittest.main()
