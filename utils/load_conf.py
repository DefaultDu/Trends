import json
import os
import sys

current_path =  os.path.dirname(os.path.dirname(__file__))
if current_path == '':
    sys.path.append(sys.path[0] + '/..')
else:
    sys.path.append(current_path +  '/..')

def load_conf():
    with open(f'{current_path}/conf/conf.json', 'r') as file:
        print(file)
        data = json.load(file)
        return data


if __name__ == '__main__':
    load_conf()