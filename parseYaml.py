import yaml

with open('test.yaml') as f:
    x = yaml.load(f)

print(x[0]['Stream'])
print(x[0]['Component'])
print(x[0]['Path'][0])
