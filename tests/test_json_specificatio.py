import unittest
import json
from src.json_specification import JSONSpecification
from io import StringIO

class TestJSONSpecification(unittest.TestCase):
    def test_read(self):
        json_data = '{"key1": "value1", "key2": "value2"}'
        json_file = StringIO(json_data)

        json_spec = JSONSpecification()
        json_spec.read(json_file)

        self.assertEqual(json_spec.spec, {"key1": "value1", "key2": "value2"})

if __name__ == "__main__":
    unittest.main()
