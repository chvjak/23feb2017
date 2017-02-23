def read_data(file_name):
    f = open(file_name)

    data = []
    for line in f:
        data += line

    return data


def write_data(file_name, data):
    f = open(file_name, "w")

    for line in data:
        f.write(line)

    f.close()