import unittest
from io import StringIO
from src.json_specification import JSONSpecification
from src.yaml_template import YamlTemplate

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        json_data = '{"key1": "value1", "key2": "new_value2"}'
        yaml_data = "key1: old_value1\nkey2: old_value2\n"

        json_file = StringIO(json_data)
        yaml_file = StringIO(yaml_data)
        output_file = StringIO()

        json_spec = JSONSpecification()
        json_spec.read(json_file)

        yaml_template = YamlTemplate()
        yaml_template.read(yaml_file)
        yaml_template.update(json_spec.spec)
        yaml_template.write(output_file)

        expected_yaml = "key1: value1\nkey2: new_value2\n"
        self.assertEqual(output_file.getvalue(), expected_yaml)

if __name__ == "__main__":
    unittest.main()
