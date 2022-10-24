#import module
import csv 

#variables


# Nom du CSV à lire
filename = "Sample.csv"
def read_csv_to_list() -> list:
    list_data = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        for line in csv_reader:
            list_data.append(line)
    return list_data

data = read_csv_to_list()
print(data)