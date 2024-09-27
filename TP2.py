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
bibliotheque = []

for row in c:
   # print(row)
    bibliotheque.append(row)

csvfile.close()

#print(bibliotheque)

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

nouvelle_coll = open('nouvelle_collection.csv', newline='')
z = csv.reader(nouvelle_coll)
boolean = False

for row in z:
        for i in bibliotheque:
            if i[3] == row[3]: print("DUPLCIATES -->", row) ; boolean=False
        if (boolean) : bibliotheque.append(row)
        boolean = True




nouvelle_coll.close()

#print(bibliotheque)



########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

for i in bibliotheque:
    i[3] = i[3].replace("S","WS")
    #print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')





########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

#ajout des clées
bibliotheque[0].append("emprunts")
bibliotheque[0].append("date_emprunt")
for i in range(1, len(bibliotheque)):
     bibliotheque[i].append("disponible")
     bibliotheque[i].append("")

#affectation de la liste emprunts.csv

emprunts = open('emprunts.csv', newline='')
y = csv.reader(emprunts)



for row in y:
     for i in range(1, len(bibliotheque)):
          if (bibliotheque[i][3] == row[0]): bibliotheque[i][4] = "emprunté" ; bibliotheque[i][5] = row[1]

emprunts.close()


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
import datetime

delaie = datetime.timedelta(days=-30)
date = datetime.date.today().__add__(delaie)

test = datetime.date(int(bibliotheque[5][5][0:4]) , int(bibliotheque[5][5][5:7]) , int(bibliotheque[5][5][8:10]))

for i in bibliotheque:
     if (i[4]== "emprunté" and datetime.date(int(i[5][0:4]), int(i[5][5:7]), int(i[5][8:10]))  < date   ): print(i)