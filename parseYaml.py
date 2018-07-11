# from ruamel.yaml import YAML
import yaml
import sys

def main():
    # yaml = YAML()
    with open('test.yaml') as f:
        deliveryTasks = yaml.load(f)
    print(deliveryTasks)

    with open('DeliveryWorkItem.yaml', 'w') as outfile:
        yaml.dump(deliveryTasks, outfile, width=4000,default_flow_style=False)

    if 'Branch' in deliveryTasks[0]:
        if(deliveryTasks[0]['Branch'] is not None and deliveryTasks[0]['Branch'].lower() != 'master'):
            raise Exception("Production delivery must delopy on master branch!")
        else:
            print('success')
    elif 'SQLCommand' in deliveryTasks:
        print ("This is SQLCommand")
    else:
        raise Exception("Error Delivery Description!")



if __name__ == '__main__':
    main()
