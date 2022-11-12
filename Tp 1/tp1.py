import math
import sys


n = 0
probabilite = []
quantiteInformation = []
somme = 0
Entropie = 0

# Saisie de la longeur de la séquence 
print()
print("Saisie de la longeur")
print("--------------------")
n = int(input("Spécifier la longeur de la séquence X : "))

print()
print()

# Saisie des probabilités 
print("Saisie des probabilité :")
print("------------------------")

for i in range(0, n):
    l = float(input("Spécifier la probabilité P({}) = ".format(i)))
    probabilite.append(l)
    somme = somme + l
    
    # Au cas ou la somme dépace 1, on termine le programme avec une erreur
    if(somme > 1):
        sys.exit("Error: The Somme of all probabilities must be equal to 1")

# Au cas ou la somme de tous les probabilités n'est pas égale a 1, on termine le programme avec une erreur
if(somme != 1):
    sys.exit("Error: The Somme of all probabilities must be equal to 1")
else:
    # Calcul des Quantité d'Information
    print()
    print()
    
    print("Les Quantités D'Informations :")
    print("------------------------------")
    
    for i in range(0, n):
        l = round(math.log2(1/probabilite[i]), 2)
        quantiteInformation.append(l)
        print("I(Pi = {}) = {}".format(i, l))
    
    # Calcul de l'Entropie
    print()
    print()
    
    print("L'Entropie :")
    print("------------")
    
    for i in range(0, n):
        Entropie = round(Entropie + (probabilite[i] * quantiteInformation[i]), 2)
        
    print("Entropie H(X) = {}".format(Entropie))
    print()