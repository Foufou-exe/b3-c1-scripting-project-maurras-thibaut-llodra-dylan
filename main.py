#import module
import csv 

#variables
filename = "conso-annuelles_v1.csv"
fileout = "conso-clean.csv"

#Fonction
def parsing_line(line) -> list:
    #init de la variable tableau 'list_element_line' qui contien tout les items de la ligne csv
    list_element_line = line
    #Suppression de la Colonnes ID_Logement
    list_element_line.pop(1)
    #Verifie s'il n'ya pas de cellule vide
    empty = False
    for element in list_element_line:
        if len(element) == 0:
            empty = True 
    if not empty:
        #Addition puis suppression des colonnes annees 1 et 2 puis resulta dans une nouvelle colonne
        annee_total = float(list_element_line[1].replace(',','.').replace('-','0')) + float(list_element_line[2].replace(',','.').replace('-','0'))
        list_element_line.pop(1)
        list_element_line.pop(1)
        list_element_line.insert(1, annee_total)
        #return de la list des elements de la ligne parser
        return list_element_line

#Tri des elemtns de la liste
def sort_list_to_csv(list_all_data):
    #init de la variable tableau 'list_all_data' qui contien tout les items de la ligne csv
    list_all_element = list_all_data
    #Tri par ordre alphabetique le type des elements de la list
    # Déclaration d'un dictionnaire vide
    dico_type = {}
    # Ajout des éléments dans le dictionnaire
    for data_list in list_all_element:
            if data_list[2] in dico_type:
                list_value_temp = dico_type[data_list[2]]
                list_value_temp.append(data_list)
                dico_type[data_list[2]] = list_value_temp
            else:
                dico_type[data_list[2]] = [data_list]
    # Tri des elements par ordre alphabetique
    for key in dico_type:
        list_keys = sorted(dico_type[key], key=lambda inner_list: inner_list[1], reverse=True)
        dico_type[key] = list_keys
    list_ordered_item = []
    # Ajouts des elements dans la list trier
    for i in sorted(dico_type.keys()):
        for item in dico_type[i]:
            list_ordered_item.append(item)
    return list_ordered_item

# Fonction d'écriture dans le nouveau fichier csv
def write_clean_list_to_csv(list_cleaned):
    with open(fileout, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list_cleaned)

def read_csv_line():
    liste_clean = []
    #liste_clean.append(['Appareil suivi', 'ID logement', 'Consommation annuelle Total(AN1+AN2)', 'Type'])
    with open(filename, 'r', encoding="latin-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        next(csv_reader)
        for line in csv_reader:
                liste_clean_temp = parsing_line(line)
                if type(liste_clean_temp) is list:
                    liste_clean.append(liste_clean_temp)
    write_clean_list_to_csv(sort_list_to_csv(liste_clean))

read_csv_line()