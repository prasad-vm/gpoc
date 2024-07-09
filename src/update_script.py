from json_specification import JSONSpecification
from yaml_template import YamlTemplate

if __name__ == "__main__":
    json_spec = JSONSpecification()
    json_spec.read('sample_files/specification.json')
    print(json_spec.read('sample_files/specification.json'))

    yaml_template = YamlTemplate()
    yaml_template.read('sample_files/template.yaml')
    print(yaml_template.read('sample_files/template.yaml'))

    yaml_template.update(json_spec.spec)
    yaml_template.write('sample_files/updated_configuration.yaml')
    print(yaml_template.write('sample_files/updated_configuration.yaml'))
