# Afi EDOH Devoir du 19/09/2023

import os
import re

# Répertoire contenant les fichiers
repertoire = "/chemin/vers/votre/repertoire"

# Expression régulière pour le format de nom de fichier
format_requis = r'^loan\d{8}\.csv$'

# Liste les fichiers dans le répertoire
fichiers = os.listdir(repertoire)

# Parcours les fichiers et vérifie le format du nom
for fichier in fichiers:
    if re.match(format_requis, fichier):
        print(f"Nom de fichier correct : {fichier}")
    else:
        print(f"Nom de fichier incorrect : {fichier}")

