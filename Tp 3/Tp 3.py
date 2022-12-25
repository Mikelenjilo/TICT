import math
import sys

#---------------------------------------------Déclaration Des Fonctions-------------------------------------------

# Fonction qui permet de repérer si la somme dépace le 1 quand on introduit les probabilités,
# et permet aussi de vérifier si la somme est égale a 1 à la fin de la saisie.
def errorChecker(a, somme):
    if(a == 0):
        # Vérifie que la somme des probabiltés ne dépace pas le 1.
        if(somme > 1):
            sys.exit("Error: The Somme of all probabilities can't be greater than 1")
    elif(a == 1):
        # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
        if(somme != 1):
            sys.exit("Error: The Somme of all probabilities must be equal to 1")


# Fonction qui permet de saisir les probabilités.
def probabilite(n, name):
    i = 0
    probabilites = []
    somme = 0

    for i in range(n):
        l = float(input("Spécifier la probabilité P({}{}) = ".format(name, i)))
        probabilites.append(l)
        somme = somme + l
        errorChecker(0, somme) # Vérifier que la somme ne dépace pas le 1.
    errorChecker(1, somme) # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
    
    return probabilites


# Fonction qui permet de calculer la quantité d'information d'une séquence.
def quantiteInformation(probabilite, n, name):
    i = 0
    quantiteInformations = []

    for i in range(n):
        l = round(math.log2(1/probabilite[i]), 2)
        quantiteInformations.append(l)
        print("I(P({}{})) = {}".format(name, i, l))

    return quantiteInformations


# Fonction qui permet de calculer l'entropie d'une séquence.
def entropie(probabilite, quantiteInformation, n, name):
    i = 0
    entropie = 0

    for i in range(n):
        entropie = round(entropie + (probabilite[i] * quantiteInformation[i]), 2)
    
    print("Entropie H({}) = {}".format(name, entropie))
    
    return entropie


# Fonction qui permet de caculer ou de saisir les probabilité mutuelles de deux séquence.
def probabiliteMutuelle(x, y, probabiliteX, probabiliteY, answer):
    probabiliteXY = []
    somme = 0
    matrice = []

    if(answer == 0): # Si les deux séquences sont dépendantes.
        print("Saisie des probabilité mutuelle des deux séquence X et Y :")
        print("----------------------------------------------------------")
        for i in range(0, x):
            for j in range(0, y):
                l = float(input("Saisie la valeur de P(X{},Y{}) : ".format(i, j))) # Saisie des probabilités
                probabiliteXY.append(l)
                somme = somme + l
            errorChecker(0, somme) # Vérifier que la somme ne dépace pas le 1.
        errorChecker(1, somme) # Vérifier que la somme égale a 1 è la fin de la saisie.

        for i in range(x): # Boucle pour pouvoir transformer la liste en matrice
            ligne = []
            for j in range(y):
                ligne.append(probabiliteXY[(x-1) * i + j])
            matrice.append(ligne)

        return matrice

    elif(answer == 1): # Si les deux séquences sont indépendantes.
        print("Calcul des probabilité mutuelle des deux séquence X et Y :")
        print("----------------------------------------------------------")
        for i in range(x):
            for j in range(y):
                l = round(probabiliteX[i] * probabiliteY[j], 2) # Calcul des probabilités
                probabiliteXY.append(l)
                print("P(X{}, Y{}) = {}".format(i, j, l))
   
        for i in range(x): # Boucle pour pouvoir transformer la liste en matrice
            ligne = []
            for j in range(y):
                ligne.append(probabiliteXY[(x-1) * i + j])
            matrice.append(ligne)

        return matrice


# Fonction qui permet de calculer la quantité d'information mutuelle.
def quantiteInformationMutuelle(x, y, probabiliteX, probabiliteY, probabiliteXY, answer):
    quantiteInformationXY = 0

    if(answer == 0): # Si les deux séquence sont dépendantes
        for i in range(x):
            for j in range(y):
                l = float(probabiliteXY[i][j] * math.log2((probabiliteXY[i][j]) / (probabiliteX[i] * probabiliteY[j])))
                quantiteInformationXY = round(quantiteInformationXY + l, 2)

    elif(answer == 1): # Si les deux séquence sont indépendantes
        quantiteInformationXY = 0
    
    print("La quantité d'information mutuelle I(X,Y) = {}".format(quantiteInformationXY))

    return quantiteInformationXY  


# Fonction qui permet de calculer l'entropie mutuelle.
def entropieMutuelle(x, y, probabiliteXY, entropiex, entropiey, answer):
    entropie = 0

    if(answer == 0): # Si les deux séquence sont dépendantes
        for i in range(x):
            for j in range(y):
                entropie = round(entropie + probabiliteXY[i][j] * math.log2(1/probabiliteXY[i][j]), 2)
    
    elif(answer == 1): # Si les deux séquence sont indépendantes
        entropie = entropiex + entropiey
    
    print("L'Entropie H(X,Y) = {}".format(entropie))

    return entropie

def probabiliteXsachantY(x, y, probabiliteY, probabiliteXY):
    somme = 0
    probabiliteXSachantY = []
    l = 0.0
    matrice = []

    for i in range(x):
        for j in range(y):
            l = round(float(probabiliteXY[i][j] / probabiliteY[j]), 2)
            probabiliteXSachantY.append(l)
            print("P(X{}, Y{}) = {}".format(i, j, l))

    for i in range(x):
        ligne = []
        for j in range(y):
            ligne.append(probabiliteXSachantY[(x-1) * i +j])
        matrice.append(ligne)

    return matrice

    
def entropieConditionnelle(x, y, probabiliteY, probabiliteXSachantY):
    somme = 0
    l = 0

    for j in range(y):
        for i in range(x):
            l = float(probabiliteY[j] * probabiliteXSachantY[i][j] * math.log2(1 / (probabiliteXSachantY[i][j])))
            somme = float(somme + l)

    
    print("L'Entropie Conditionnelle H(X|Y) = {}".format(somme))
    return somme


    
#---------------------------------------------Code Principale---------------------------------------------

x = 0
y = 0
probabiliteX = []
probabiliteY = []
probabiliteXY = []
quantiteInformationX = []
quantiteInformationY = []
quantiteInformationXY = 0
probabiliteXSachantY = []
sommeX = 0
sommeY = 0
EntropieX = 0
EntropieY = 0
EntropieXY = 0
entropieC = 0

# Saisie de la longeur de la séquence X
print()
print("Saisie de la longeur de la séquence X :")
print("---------------------------------------")
x = int(input("Spécifier la longeur de la séquence X  : "))
print()

# Saisie de la longeur de la séquence Y
print()
print("Saisie de la longeur de la séquence Y :")
print("---------------------------------------")
y = int(input("Spécifier la longeur de la séquence Y : "))
print()

# Les deux séquences sont indépendantes ou non ?
answer = int(input("Les deux séquences sont indépendantes ou non ? (oui = 1, non = 0) : "))
print()

# Saisie des probabilités de la séquence X
print("Saisie des probabilité de la séquence X:")
print("----------------------------------------")
probabiliteX = probabilite(x, "X")
print()

# Saisie des probabilités de la séquence Y
print("Saisie des probabilité de la séquence Y:")
print("----------------------------------------")
probabiliteY = probabilite(y, "Y")
print()


# Saisie ou Calcul des probabilitées mutuelles X,Y selon la réponse
probabiliteXY = probabiliteMutuelle(x, y, probabiliteX, probabiliteY, answer)

# Calcul des Quantité d'Information
print()
print("Les Quantités D'Informations I(X):")
print("----------------------------------")
quantiteInformationX = quantiteInformation(probabiliteX, x, "X")

print()
print("Les Quantités D'Informations I(Y):")
print("----------------------------------")
quantiteInformationY = quantiteInformation(probabiliteY, y, "Y")

print()

# Calcul de la Quantité d'Information Mutuelle I(X,Y)
print()
print("Les Quantités D'Informations I(X, Y):")
print("-------------------------------------")
quantiteInformationXY = quantiteInformationMutuelle(x, y, probabiliteX, probabiliteY, probabiliteXY, answer)
print()


# Calcul de l'Entropie H(X)
print()
print("L'Entropie H(X) :")
print("-----------------")
EntropieX = entropie(probabiliteX, quantiteInformationX, x, "X")
print()

# Calcul de l'Entropie H(Y)
print()
print("L'Entropie H(Y) :")
print("-----------------")
EntropieY = entropie(probabiliteY, quantiteInformationY, y, "Y")

# Calcul de l'Entropie mutuelle H(X,Y)
print()
print("L'Entropie H(X,Y) : ")
print("--------------------")
EntropieXY = entropieMutuelle(x, y, probabiliteXY, EntropieX, EntropieY, answer)
print()

# Loi de Bayes P(xi|yj) = P(xi,yj) / P(yj)
print()
print("La probabilté de X sachant Y : ")
print("-------------------------------")
probabiliteXSachantY = probabiliteXsachantY(x, y ,probabiliteY, probabiliteXY)
print()

# Calcul de l'Entropie conditionnelle H(X|Y) = Somme(P(yi))*Somme(P(xi|yj)*log2(1/P(xi|yj)))
print()
print("L'Entropie conditionnelle H(X|Y) : ")
print("------------------------------------")
entropieC = entropieConditionnelle(x, y, probabiliteY, probabiliteXSachantY) 
print()
