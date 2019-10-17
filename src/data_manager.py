import csv, os, glob
from src.data import Data


def list_files():
    try:
        return glob.glob("./input/*.csv")
    except Exception as err:
        print(err)


def save_file(filename, data):
    os.makedirs("./output/", exist_ok=True)
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
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = Data(row["email"], row["gender"], row["uid"], row["birthdate"], row["height"], row["weight"])
                vector.append(data)
    except Exception as err:
        print(err)

    return vector


def is_sorted(vector):
    for i in range(len(vector) - 1):
        if vector[i].bigger_than(vector[i + 1]):
            return False
    return True
