import yaml

with open('config.yml','r') as f:
    config = yaml.load(f)
with open('secrets.yml','r') as f:
    secrets = yaml.load

# print(config['favEditor'])
