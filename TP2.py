"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  03
Noms et matricules : Abbas, Usalas (Matricule1), Nguyen Le, William (2393842)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

bibliotheque = {}

csvfile = open("collection_bibliotheque.csv")
c = csv.reader(csvfile)
next(c)
for row in c:
    titre, auteur, date_publication, cote_rangement = row
    bibliotheque[cote_rangement] = {
        "titre" : titre,
        "auteur" : auteur,
        "date_publication" : date_publication
    }
csvfile.close()
print(bibliotheque["P021"])
#print(bibliotheque["H007"])
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

#IL Y A 24 AJOUTÉ ET 6 DUP

N_csvfile = open("nouvelle_collection.csv")
N_c = csv.reader(N_csvfile)
next(N_c)

for N_row in N_c:
    N_titre, N_auteur, N_date_publication, N_cote_rangement = N_row

    # Check if the cote_rangement is already in the bibliotheque
    if N_cote_rangement in bibliotheque:
        print(f"Le livre {N_cote_rangement} ---- {N_titre} par {N_auteur} ---- est déjà présent dans la bibliothèque")
    else:
        bibliotheque[N_cote_rangement] = {
            "titre": N_titre,
            "auteur": N_auteur,
            "date_publication": N_date_publication
        }
        print(f"Le livre {N_cote_rangement} ---- {N_titre} par {N_auteur} ---- a été ajouté avec succès")

N_csvfile.close()

print(f'\n Bibliotheque finale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
N_bibliotheque = {}
for key in bibliotheque:
    if bibliotheque[key]['auteur'] == "William Shakespeare":
        N_key = "WS" + key[1:]
        N_bibliotheque[N_key] = bibliotheque[key]
    else:
        N_bibliotheque[key] = bibliotheque[key]

bibliotheque = N_bibliotheque
#for key in bibliotheque:
#    if key[0:1] == ["WS"]:
#        print(bibliotheque[key])

print(f'\n Bibliotheque avec modifications de cote : {bibliotheque} \n')





########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici


