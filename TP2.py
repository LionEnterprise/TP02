"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  03
Noms et matricules : Abbas, Usalas (2383986), Nguyen Le, Williamg (2393842)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

csvfile = open('collection_bibliotheque.csv', newline='')
c = csv.reader(csvfile)
bibliotheque = {}

for row in c:
     info = {}
     info["titre"] = row[0]
     info["auteur"] = row[1]
     info["date_publication"] = row[2]
     bibliotheque[row[3]] = info

csvfile.close()
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

#print(bibliotheque)

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

nouvelle_coll = open('nouvelle_collection.csv', newline='')
z = csv.reader(nouvelle_coll)

for row in z:
     if (row[3] in bibliotheque): print("Le livre {row[3]} ---- {row[0]} par {row[1]} ---- est déjà présent dans la bibliothèque")
     else: print("Le livre {row[3]} ---- {row[0]} par {row[1]} ---- a été ajouté avec succès")
     info = {}
     info["titre"] = row[0]
     info["auteur"] = row[1]
     info["date_publication"] = row[2]
     bibliotheque[row[3]] = info

nouvelle_coll.close()




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

#for i in bibliotheque:
#    i[3] = i[3].replace("S","WS")
#    #print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

change_list = []
for i in bibliotheque.values():
    if "William Shakespeare" in i["titre"]: change_list.append(i)

for i in change_list:
     bibliotheque["W" + i] = bibliotheque.pop(i)


print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

#affectation de la liste emprunts.csv

#ajout des clées
for i in bibliotheque:
     bibliotheque[i]["emprunts"] = "disponible"
     bibliotheque[i]["date_emprunt"] = ""

emprunts = open('emprunts.csv', newline='')
y = csv.reader(emprunts)


for row in y:
     bibliotheque[row[0]]["emprunts"] = "emprunté"
     bibliotheque[row[0]]["date_emprunt"] = row[1]

bibliotheque["cote_rangement"]["emprunts"] = "disponible"

emprunts.close()

print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
import datetime

delaie = datetime.timedelta(days=-30)
date = datetime.date.today().__add__(delaie)

for i in bibliotheque:
     bibliotheque[i]["frais_retard"] = 0
     bibliotheque[i]["livre_perdus"] = "non"

for i in bibliotheque.values():
     if (i["emprunts"]== "emprunté"):
          date_emprunt = datetime.date(int(i["date_emprunt"][0:4]), int(i["date_emprunt"][5:7]), int(i["date_emprunt"][8:10]))
          delaie_emprunt = (date - date_emprunt)
          if ( 50 >= delaie_emprunt.days > 30):
            i["frais_retard"] = delaie_emprunt.days*2
          if (delaie_emprunt.days > 50):
               i["frais_retard"] = 100
          if (delaie_emprunt.days > 365):
               i["livre_perdus"] = "oui"

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')