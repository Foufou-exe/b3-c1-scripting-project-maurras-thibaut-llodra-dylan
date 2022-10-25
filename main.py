#import module
import csv 

#variables
filename = "conso-annuelles_v1.csv"
fileout = "clean.csv"

#Fonction
def parsing_line(line) -> list:
    #init de la variable tableau 'list_element_line' qui contien tout les items de la ligne csv
    list_element_line = line
    #Suppression des Colonnes A,D,E,F,G
    
    
    #Verifie s'il n'ya pas de cellule vide
    empty = False
    for element in list_element_line:
        if len(element) == 0:
            empty = True
    if not empty:
        #return de la list des elements de la ligne parser
        return list_element_line

def write_clean_list_to_csv(list_cleaned):
    with open(fileout, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list_cleaned)

def read_csv_line():
    liste_clean = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        next(csv_reader)
        for line in csv_reader:
            liste_clean_temp = parsing_line(line)
            if type(liste_clean_temp) is list:
                liste_clean.append(liste_clean_temp)
    write_clean_list_to_csv(liste_clean)

read_csv_line()