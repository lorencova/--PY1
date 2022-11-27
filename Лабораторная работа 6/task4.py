import json

INPUT_FILE = "input1.csv"


def csv_to_list_dict(filename):
    list_dict = []
    list_rows = []
    with open(filename, "r") as f:
        res = f.readlines()
        headers = res[0].rstrip().split(',')
        for row in res[1:]:
            list_rows.append(row.rstrip().split(','))

        for el in list_rows:
            a = {k: v for k, v in zip(headers, element)}
            list_dik.append(a)

# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent = 4))
