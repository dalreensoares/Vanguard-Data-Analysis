import yaml

with open('config.yaml', 'r') as config_file:
  config = yaml.safe_load(config_file)

csv_path = config['name_in_yalm']