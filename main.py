#import module

import csv 

# Nom du CSV à lire
filename = "b3-c1-scripting-project-maurras-thibaut-llodra-dylan/Sample.csv"
def list_csv() -> list:
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        for line in csv_reader:
            print(line)

list_csv()
        