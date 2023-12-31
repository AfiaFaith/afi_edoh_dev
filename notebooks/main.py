import os
import re
import argparse
import sys

# Fonction de configuration pour gérer les arguments de ligne de commande
def configurer_arguments():
    parser = argparse.ArgumentParser(description="Vérification des noms de fichiers au format 'loanYYYYMMDD.csv'")
    parser.add_argument("repertoire", help="Chemin vers le répertoire contenant les fichiers à vérifier")
    parser.add_argument("-o", "--output", help="Chemin du fichier de sortie pour enregistrer les résultats")
    return parser.parse_args()

# Fonction pour vérifier le format du nom de fichier et enregistrer les résultats
def verifier_format_nom_fichier(repertoire, fichier_sortie=None):
    # Expression régulière pour le format de nom de fichier "loanYYYYMMDD.csv"
    format_nom_fichier = r'^loan\d{8}\.csv$'

    # Vérifie l'existence du répertoire
    if not os.path.exists(repertoire):
        print(f"Le répertoire spécifié '{repertoire}' n'existe pas.")
        return

    try:
        # Liste les fichiers dans le répertoire spécifié
        fichiers = os.listdir(repertoire)

        # Ouvre le fichier de sortie s'il est spécifié
        if fichier_sortie:
            sortie = open(fichier_sortie, 'w')
        else:
            sortie = sys.stdout

        # Parcours les fichiers et vérifie le format du nom
        for fichier in fichiers:
            if re.match(format_nom_fichier, fichier):
                sortie.write(f"Nom de fichier correct : {fichier}\n")
            else:
                sortie.write(f"Nom de fichier incorrect : {fichier}\n")

        # Ferme le fichier de sortie s'il a été ouvert
        if fichier_sortie:
            sortie.close()
    except OSError as e:
        print(f"Erreur lors de la lecture du répertoire : {e}")

if __name__ == "__main__":
    # Configuration des arguments de ligne de commande
    args = configurer_arguments()

    # Vérification du format du nom de fichier dans le répertoire spécifié
    verifier_format_nom_fichier(args.repertoire, args.output)
