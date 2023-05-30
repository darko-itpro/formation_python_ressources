
def load_from_csv(path):
    with open(path) as csv_file:
        csv_file.readline()
        for line in csv_file:
            yield line.split(';')

