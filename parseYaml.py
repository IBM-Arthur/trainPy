import yaml

with open('test.yaml') as f:
    x = yaml.load(f)

print(x)
for i in range(int(len(x))):
    print(x[i]['Stream'])
    print(x[i]['Component'])
    for j in range(int(len(x[i]['Path']))):
        print(x[i]['Path'][j])
