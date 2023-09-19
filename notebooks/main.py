# Afi EDOH Devoir du 19/09/2023

import os
import re
import argparse

# Fonction de configuration pour gérer les arguments de ligne de commande
def configurer_arguments():
    parser = argparse.ArgumentParser(description="Vérification des noms de fichiers au format 'loanYYYYMMDD.csv'")
    parser.add_argument("repertoire", help="Chemin vers le répertoire contenant les fichiers à vérifier")
    return parser.parse_args()

# Fonction pour vérifier le format du nom de fichier
def verifier_format_nom_fichier(repertoire):
    # Expression régulière pour le format de nom de fichier "loanYYYYMMDD.csv"
    format_nom_fichier = r'^loan\d{8}\.csv$'

    try:
        # Liste les fichiers dans le répertoire spécifié
        fichiers = os.listdir(repertoire)

        # Parcours les fichiers et vérifie le format du nom
        for fichier in fichiers:
            if re.match(format_nom_fichier, fichier):
                print(f"Nom de fichier correct : {fichier}")
            else:
                print(f"Nom de fichier incorrect : {fichier}")
    except OSError as e:
        print(f"Erreur lors de la lecture du répertoire : {e}")

if __name__ == "__main__":
    # Configuration des arguments de ligne de commande
    args = configurer_arguments()

    # Vérification du format du nom de fichier dans le répertoire spécifié
    verifier_format_nom_fichier(args.repertoire)



