import json


def dict_magic(d, prev='', sep='__'):
    if isinstance(d, dict):
        for k, v in d.items():
            dict_magic(v, prev=prev+sep+str(k))
    else:
        print(prev+'='+str(d))


if __name__ == '__main__':
    # path to json file
    json_file = input()
    with open(json_file, mode='r') as file:
        j = json.load(file)
        dict_magic(j)

