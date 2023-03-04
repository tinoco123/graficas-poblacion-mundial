import csv


def read_csv(path):
    data = []
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)
        for row in reader:
            data_in_dict = {}
            iterable = zip(header, row)
            data_in_dict = dict(iterable)  # {key: value for key, value in iterable}
            data.append(data_in_dict)
        return data


def get_header(path):
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)
        return header