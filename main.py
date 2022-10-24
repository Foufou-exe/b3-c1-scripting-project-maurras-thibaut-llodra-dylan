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

def parsing_line(line) -> list:
    #init de la variable tableau 'list_element_line' qui contien tout les items de la ligne csv
    list_element_line = line
    #Suppression des Colonnes A,D,E,F,G
    list_element_line.pop(0)
    list_element_line.pop(2)
    list_element_line.pop(2)
    list_element_line.pop(2)
    list_element_line.pop(2)
    #Supprimer toutes les lignes avec moins une cellule vide
    for element in list_element_line:
        if element != "" :
            #return de la list des elements de la ligne parser
            return list_element_line
