import csv, os, glob, sys
from data import Data
from record import Record

_INPUT_PATH = "./src/input/"
_OUTPUT_PATH = "./src/output/"
_RECORD_FILE = "records.csv"


def list_files():
    files = []
    try:
        files_path = glob.glob(_INPUT_PATH + "*.csv")
        for f in files_path:
            if sys.platform == "win32":
                files.append(f.split("\\")[-1])
            else:
                files.append(f.split("/")[-1])
        return files
    except Exception as err:
        print(err)


def save_file(filename, data):
    os.makedirs(_OUTPUT_PATH, exist_ok=True)
    print("Sorted %s:" % str(is_sorted(data)))
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
        with open(os.path.join(_OUTPUT_PATH, filename), 'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataCSV)
    except Exception as err:
        print("Erro ao salvar: %s" % (err))


def save_record_time(data):
    os.makedirs(_OUTPUT_PATH, exist_ok=True)
    dataCSV = []
    try:
        f = open(os.path.join(_OUTPUT_PATH, _RECORD_FILE), 'r')
        f.close()
    except:
        head = ["algorithm", "size", "min", "max", "avg", ]
        dataCSV = [head]

    try:

        for p in data:
            dataCSV.append(p)
        with open(os.path.join(_OUTPUT_PATH, _RECORD_FILE), 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataCSV)
    except Exception as err:
        print(err)


def open_record_time():
    vector = []
    try:
        with open(_INPUT_PATH + _RECORD_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = Record(row["algorithm"], row["times"], row["min"], row["max"], row["avg"])
                vector.append(data)
    except Exception as err:
        return None
    return vector


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
