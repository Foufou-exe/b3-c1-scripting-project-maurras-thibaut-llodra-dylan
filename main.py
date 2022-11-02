#import module csv pour la lecture et l'ecriture du ficher
import csv 
import argparse
import logging

# Option de lancement
parser = argparse.ArgumentParser(description='INFO : Les options permettent de choisir les fichiers en entrer et en sortie')
parser.add_argument('-s', '--source', type=str, help='Source du fichier comprenant l\'extension .csv')
parser.add_argument('-o', '--output', type=str, help='Sortie du fichier comprenant l\'extension .csv')
arguments = parser.parse_args()

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
)

#variables
#nom du ficher d'entree
filename = "conso-annuelles_v1.csv"
# Verifie si l'argument donne fini par .csv
if arguments.source and arguments.source.endswith('.csv') :
    filename = arguments.source
    

#nom du ficher de sorti
fileout = "conso-clean.csv"
# Verifie si l'argument donne fini par .csv
if arguments.output and arguments.output.endswith('.csv'):
    fileout = arguments.output

#Fonction
def parsing_line(line) -> list:
    try:
        #init de la variable tableau 'list_element_line' qui contien tout les items de la ligne csv
        list_element_line = line
        #Suppression de la Colonnes ID_Logement
        list_element_line.pop(1)
        #Verifie s'il n'ya pas de cellule vide
        empty = False
        #pour chaque element de la liste de la ligne csv
        for element in list_element_line:
            #Si la longeur de lelement est 0 (il est nul)
            if len(element) == 0:
                #changement de la valeur empty pour signaler une ligne vide
                empty = True 
        logging.info('Element trier si cellule vide')
        #Si il n'y a pas de ligne vide
        if not empty:
            #Addition puis suppression des colonnes annees 1 et 2 puis resulta dans une nouvelle colonne
            #variable avec le resultat de l'adition des deux colonne annuelle
            annee_total = float(list_element_line[1].replace(',','.').replace('-','0')) + float(list_element_line[2].replace(',','.').replace('-','0'))
            #suppression de la colone ID_logement
            list_element_line.pop(1)
            #suppression de la colone Consommation annuelle AN1
            list_element_line.pop(1)
            #remplacement de la valeur de la colone Consommation annuelle AN2 en colonne totak annees
            list_element_line.insert(1, annee_total)
            logging.info('Liste formater avec les nouvelles colonnes')
            #return de la list des elements de la ligne parser
            return list_element_line
    except Exception as e:
        logging.error(e)
    
    
#Tri des elemtns de la liste
def sort_list_to_csv(list_all_data) -> list:
    try:
        #init de la variable tableau 'list_all_data' qui contien tout les items de la ligne csv
        list_all_element = list_all_data
        #Tri par ordre alphabetique le type des elements de la list
        # Déclaration d'un dictionnaire vide
        dico_type = {}
        #Pour chaque liste de data dans la liste d'element
        for data_list in list_all_element:
                #si le type de l'element est dans le dictionnaire d'element alors
                if data_list[2] in dico_type:
                    #recuperation de la liste des liste des information des element avec comme cle le type dans le dictionnaore
                    list_value_temp = dico_type[data_list[2]]
                    #Ajout a la liste des elements de la cle le nouvelle element qui a le type
                    list_value_temp.append(data_list)
                    #Mise a jour de la valeur de la cle avec la nouvelle liste
                    dico_type[data_list[2]] = list_value_temp
                #sinon le type de l'element n'est pas dans le dictionnaire d'element alors
                else:
                    #ajout dans le dictionnaire avec comme clé le type de l'element et comme valeur une nouvelle liste avec comme premiere element la lisre avec toutes les information de l'element
                    dico_type[data_list[2]] = [data_list]
        logging.info('Dictionnaire des types d\'elements créent avec succes')
        # Tri des elements par ordre decroissent de la consomation annuelle
        #pour chaque clé dans le dictionnaire 
        for key in dico_type:
            #tri du type de la consommation annuelle dans l'ordre decroissent
            list_keys = sorted(dico_type[key], key=lambda inner_list: inner_list[1], reverse=True)
            #Mise a jour de la cle avec la nouvelle liste d'element trier
            dico_type[key] = list_keys
        logging.info('Pour chaque type d\'appareils la liste d\'element est trier par consommation annuel par decroissant')
        #creation d'une liste vide
        list_ordered_item = []
        #Pour chaque cle dans l'ordre alaphabetic du dictionnaire
        for i in sorted(dico_type.keys()):
            #Pour chaque list d'elemtn pour la valeur de la cle i
            for item in dico_type[i]:
                #Ajout de la liste dans la liste temp
                list_ordered_item.append(item)
        #ajout du nom de chque colonne
        list_ordered_item.insert(0, ['Appareil suivi', 'Consommation annuelle Total(AN1+AN2)', 'Type']) 
        #Retour de la fonction en liste d'elemtn 
        logging.info('Type d\'appareils trier par ordre alphabétique')
        return list_ordered_item
    except Exception as e:
        logging.error(e)


# Fonction d'écriture dans le nouveau fichier csv
def write_clean_list_to_csv(list_cleaned) -> None:
    try:
        #ouvrir le fichier en mode ecriture et enoding en latin-1
        with open(fileout, 'w', encoding="latin-1") as csv_file:
            logging.info(f'Fichier ({fileout}) ouvert avec succès.')
            #enregistrement du writer de csv dans une variable 
            writer = csv.writer(csv_file)
            #ecriture de la liste dans le fichier
            writer.writerows(list_cleaned)
            logging.info(f'Fichier ({fileout}) écrit avec succès.')
    except Exception as e:
        logging.error(e)


#lire les elements du csv
def read_csv_line() -> None:
    try:
        #creation d'une ligne vide qui va contenir les elements du csv clean
        liste_clean = []
        #ouvre le fichier csv en lecture et avec latin1 en encoding dans le nom de variable = csv_file
        with open(filename, 'r', encoding="latin-1") as csv_file:
            #cree la varible csv_reader grace au delimiter ; et au fichier ouvert
            csv_reader = csv.reader(csv_file, delimiter = ';')
            #saute la premiere ligne du fichier csv
            next(csv_reader)
            logging.info(f'Fichier ({filename}) ouvert avec succès.')
            #pour chaque ligne du csv executer le code suivant
            for line in csv_reader:
                    #recuperation de la ligne actuelle parsé avec les tri demander et stocker dans une variable
                    liste_clean_temp = parsing_line(line)
                    #si le type de sortie stocker dans la variable est une liste alors 
                    if type(liste_clean_temp) is list:
                        #ajoyter a la liste clean declarer au debut la vaiable temp
                        liste_clean.append(liste_clean_temp)
        #le fichier csv se referme apres la lecture de toutes les lignes et envoie le tableau avec toute les ligne parsé dans le trieur puis dans le ficher de sortie
        write_clean_list_to_csv(sort_list_to_csv(liste_clean))
        logging.info(f'Fichier ({filename}) nettoyer avec succès, nouveau fichier propre crée ({fileout}).')
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
   read_csv_line()