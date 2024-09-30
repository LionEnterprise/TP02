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
print(bibliotheque["H007"])
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
#i=1
#csvfile = open('nouvelle_collection.csv', newline='')
#c = csv.reader(csvfile)
#print(len(cote_rangement))
#for ligne in c:
    #while i < len(cote_rangement):
        #if cote_rangement[i] == ligne[3]:
            #print("")
            #print(f"Le livre {cote_rangement[i]} ---- {titre[i]} par {auteur[i]} ---- a été ajouté avec succès")
            #print(cote_rangement[i])
            #print(ligne[3])
        #else:
            #print("")
            #print(fLe livre {cote_rangement[i]} ---- {titre[i]} par {auteur[i]} ---- est déjà présent dans la bibliothèque")
            #print(cote_rangement[i])
            #print(ligne[3])
            #print(i)
        #i = i+1
    #print(i)
#csvfile.close()





########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici


