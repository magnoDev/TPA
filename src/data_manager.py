import csv, os, glob
from data import Data

_INPUT_PATH = "./src/input/"
_OUTPUT_PATH = "./src/output/"


def list_files():
    try:
        return glob.glob(_INPUT_PATH + "*.csv")
    except Exception as err:
        print(err)


def save_file(filename, data):
    os.makedirs(_OUTPUT_PATH, exist_ok=True)
    try:
        head = ["email", "gender", "uid", "birthdate", "height", "weight"]
        dataCSV = [head]
        for p in data:
            dataCSV.append([
                p.email,
                p.gender,
                p.uid,
                p.birthdate,
                p.height,
                p.weight
            ])
        with open(os.path.join("./output/", filename), 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataCSV)
    except Exception as err:
        print(err)


def open_input_file(file):
    vector = []
    try:
        with open(_INPUT_PATH + file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = Data(row["email"], row["gender"], row["uid"], row["birthdate"], row["height"], row["weight"])
                vector.append(data)
    except Exception as err:
        print("Erro ao abrir o arquivo: %s " % err)
    return vector


def is_sorted(vector):
    for i in range(len(vector) - 1):
        if vector[i].bigger_than(vector[i + 1]):
            return False
    return True
