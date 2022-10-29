"""
TODO: I(x) Done
* I(x) = 1/log2(P(x))

TODO: I(y) Done
* I(y) = 1/log2(P(y))

TODO: H(x) Done 
* H(x) = Somme de P(x) * log2(1/P(x))
* Let the user enter the probabilities for the X sequence

TODO: H(y) Done
* H(y) = Somme de P(y) * log2(1/P(y))
* Let the user enter the probabilities for the Y sequence

TODO: P(x,y) Done
* Let the user enter teh probabilities for the P(x,y),
* and let him choose if the two sequences are independents or not

TODO: I(x,y)
* IF the two sequences are independents so I(x,y) = 0, else => I(x,y) != 0

TODO: H(x,y) Done
* H(x,y) = Somme de P(x,y) * log2(1/P(x,y)) 

"""

import math
import sys

def errorChecker(a, somme):
    if(a == 0):
        if(somme > 1):
            sys.exit("Error: The Somme of all probabilities can't be greater than 1")
    elif(a == 1):
        if(somme != 1):
            sys.exit("Error: The Somme of all probabilities must be equal to 1")


def probabilite(n, name):
    i = 0
    probabilites = []
    somme = 0
    for i in range(n):
        l = float(input("Spécifier la probabilité P({}{}) = ".format(name, i)))
        probabilites.append(l)
        somme = somme + l
        errorChecker(0, somme)
    errorChecker(1, somme)
    return probabilites

def quantiteInformation(probabilite, n, name):
    i = 0
    quantiteInformations = []
    for i in range(n):
        l = round(math.log2(1/probabilite[i]), 2)
        quantiteInformations.append(l)
        print("I(P({}{})) = {}".format(name, i, l))
    return quantiteInformations

def entropie(probabilite, quantiteInformation, n, name):
    i = 0
    entropie = 0
    for i in range(n):
        entropie = round(entropie + (probabilite[i] * quantiteInformation[i]), 2)

    print("Entropie H({}) = {}".format(name, entropie))
    return entropie

def quantiteInformationMutuelle(n, probabiliteXY, probabiliteX, probabiliteY):
    quantiteInformationXY = 0

    if(answer == 0):
        for i in range(0, n):
            for j in range(0, n):
                l = float(round(probabiliteXY[i][j] * math.log2((probabiliteXY[i][j]) / (probabiliteX[i] * probabiliteY[j])), 2))
                quantiteInformationXY = quantiteInformationXY + l
    elif(answer == 1):
        quantiteInformation = 0
    print("La quantité d'information mutuelle I(X,Y) = {}".format(quantiteInformationXY))
    return quantiteInformationXY  


    return quantiteInformationXY

def probabiliteMutuelle(n):
    probabiliteXY = []
    for i in range(0, n):
        somme = 0
        for j in range(0, n):
            l = float(input("Saisie la valeur de P(X{},Y{}) : ".format(i, j)))
            probabiliteXY.append(l)
            somme = somme + l
            errorChecker(0, somme)
        errorChecker(1, somme)
                

    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(probabiliteXY[n * i + j])
        matrice.append(ligne)
    
    return matrice

def entropieMutuelle(n, probabiliteXY, entropiex, entropiey, answer):
    entropie = 0
    if(answer == 0):
        for i in range(0, n):
            for j in range(0, n):
                entropie = round(entropie + probabiliteXY[i][j] * math.log2(1/probabiliteXY[i][j]), 2)
    
    elif(answer == 1):
        entropie = entropiex + entropiey
    
    print("L'Entropie H(X,Y) = {}".format(entropie))
    return entropie

n = 0
probabiliteX = []
probabiliteY = []
probabiliteXY = []
quantiteInformationX = []
quantiteInformationY = []
quantiteInformationXY = 0
sommeX = 0
sommeY = 0
EntropieX = 0
EntropieY = 0
EntropieXY = 0

# Saisie de la longeur de la séquence X et de la séquence Y
print()
print("Saisie de la longeur de la séquence X et de la séquence Y :")
print("-----------------------------------------------------------")
n = int(input("Spécifier la longeur de la séquence X et de la séquence Y : "))

print()

answer = int(input("Les deux séquence sont indépendantes ou non ? (oui = 1, non = 0) : "))

print()

# Saisie des probabilités de la séquence X
print("Saisie des probabilité de la séquence X:")
print("----------------------------------------")
probabiliteX = probabilite(n, "X")
print()

# Saisie des probabilités de la séquence Y
print("Saisie des probabilité de la séquence Y:")
print("----------------------------------------")
probabiliteY = probabilite(n, "Y")
print()

# Saisie des probabilitées mutuelles X,Y si 
print("Saisie des probabilité mutuelle des deux séquence X et Y :")
print("----------------------------------------------------------")
probabiliteXY = probabiliteMutuelle(n)

# Calcul des Quantité d'Information
print()

print("Les Quantités D'Informations I(X):")
print("----------------------------------")
quantiteInformationX = quantiteInformation(probabiliteX, n, "X")

print()
print("Les Quantités D'Informations I(Y):")
print("----------------------------------")
quantiteInformationY = quantiteInformation(probabiliteY, n, "Y")

print()

# Calcul de la Quantité d'Information Mutuelle I(X,Y)
print()
print("Les Quantités D'Informations I(X, Y):")
print("-------------------------------------")
quantiteInformationXY = quantiteInformationMutuelle(n, probabiliteXY, probabiliteX, probabiliteY)

print()


# Calcul de l'Entropie H(X)
print()

print("L'Entropie H(X) :")
print("-----------------")
EntropieX = entropie(probabiliteX, quantiteInformationX, n, "X")

print()

# Calcul de l'Entropie H(Y)
print()

print("L'Entropie H(Y) :")
print("-----------------")
EntropieY = entropie(probabiliteY, quantiteInformationY, n, "Y")

# Calcul de l'Entropie mutuelle H(X,Y)
print()

print("L'Entropie H(X,Y) : ")
print("--------------------")
EntropieXY = entropieMutuelle(n, probabiliteXY, EntropieX, EntropieY, answer)


print()