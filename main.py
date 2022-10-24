#import module
import csv 

#variables
filename = "Sample.csv"
fileout = "clean.csv"

#Fonction
def read_csv_line():
    liste_clean = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        for line in csv_reader:
            liste_clean.append(parsing_line(line))
    write_clean_list_to_csv(liste_clean)

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
    
def write_clean_list_to_csv(list_cleaned):
    with open(fileout, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list_cleaned)


read_csv_line()




#### COMPREHENSION


# A B C D E F G H I J 
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8 
#   0 1 - 2 3 4 5 6 7 
#   0 1 - - 2 3 4 5 6 
#   0 1 - - - 2 3 4 5 
#   0 1 - - - - 2 3 4 
#['8152'=A 0, '6160'=B 1, 'Alan Dominguez'=C 2, '3746'=D 3, '162.67'=E 4 , '115.99'=F 5, '2.5'=G 6, 'Alberta'=H 7, 'Telephones and Communication'=I 8, '0.57'=J 9]
#Suppression des Colonnes A,D,E,F,G
#garde des Colonnes B,C,H,I,J

# 7145, A 
# "Telephone Message Books with Fax/Mobile Section,  B
# 4 1/4"" x 6""", C
# Jill Matthias, D
# 43846, E
# -8.28, F
# 3.6,2.2, G 
# British Columbia, H
# Paper, I 
# 0.39 J

#['Telephone Message Books with Fax/Mobile Section, 4 1/4" x 6"', 'Jill Matthias', '43846', 'British Columbia', 'Paper', '0.39']