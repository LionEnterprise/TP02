import csv
from datetime import datetime
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
#print(bibliotheque["P021"])
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

print(f'\n Bibliotheque avec modifications de cote : {bibliotheque} \n')





########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

emprunts = {}
csvfile = open("emprunts.csv")
c = csv.reader(csvfile)
next(c)
for row in c:
    cote_rangement, date_emprunt = row
    emprunts[cote_rangement] = date_emprunt

for cle in bibliotheque:
    if cle in emprunts:
        bibliotheque[cle]["emprunts"] = "emprunté"
        bibliotheque[cle]["date_emprunt"] = emprunts[cle]
    else:
        bibliotheque[cle]["emprunts"] = "disponible"
        bibliotheque[cle]["date_emprunt"] = None

print(f'\n Bibliotheque avec modifications de cote : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

date_mtn = (datetime.now())
            #.strftime("%Y-%m-%d"))
difference_date = 0
for cle in bibliotheque:
    if bibliotheque[cle]['emprunts'] == "emprunté":
        date_emprunt = datetime.strptime(bibliotheque[cle]['date_emprunt'], "%Y-%m-%d")
        difference_date = (date_mtn - date_emprunt).days

        if difference_date <30:
            bibliotheque[cle]["frais_retard"] = difference_date*2
            print(bibliotheque[cle])

        elif difference_date > 50 and difference_date < 365:
            bibliotheque[cle]["frais_retard"] = "100"
            print(bibliotheque[cle])

        else:
            bibliotheque[cle]["livres_perdus"] = "Perdu"

#    else:
#        bibliotheque[cle]["frais_retard"] = None

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')