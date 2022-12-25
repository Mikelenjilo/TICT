import sys
import math

#-------------------------------------------------Déclaration des Functions------------------------------------------------
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

def errorChecker(a, somme):
    if(a == 0):
        # Vérifie que la somme des probabiltés ne dépace pas le 1.
        if(somme > 1):
            sys.exit("Erreur : La somme des probabilitées ne peut pas être supérieur a 1")
    elif(a == 1):
        # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
        if(somme != 1):
            sys.exit("Erreur : La somme des probabilitées doit être égale a 1")

def entropie(probabilite, n, name):
    i = 0
    entropie = 0

    for i in range(n):
        entropie = round(entropie + (probabilite[i] * math.log2(1/probabilite[i])), 2)
    
    print("Entropie H({}) = {} Bits/symbole".format(name, entropie))
    
    return entropie

def longeurMoyenne(probabilite, n, code):
    R = 0

    for i in range(n):
        R = round(R + len(code[i]) * probabilite[i], 2)

    return R

def codeF(n):
    i = 0
    l = 0
    a = True
    t = 0
    code = []

    for i in range(n):
        l = input("Donner le code correspondant qu élémenet n°{} : ".format(i))
        code.append(l)

    for i in range(n):
        for j in range(n):
            if(len(code[i]) < len(code[j])):
                t = code[j]
                code[j] = code[i]
                code[i] = t
    
    for i in range(0, x-1):
        for j in range(i+1, x):
            if(code[j].startswith(code[i])):
                a = False
    
    print("")
    print("Le Type de Code :")
    print("-----------------")

    if(a == True):
        print("Le code est préfix")
    else:
        print("Le code n'est pas préfix")

    return code
#-------------------------------------------------Code Principale------------------------------------------------
codeA = []
i = 0
j = 0
a = True

print()
print("Saisie de la longeur de la séquence X :")
print("---------------------------------------")
x = int(input("Spécifier la longeur de la séquence X  : "))
print()
print("Saisie des probabilité de la séquence X:")
print("----------------------------------------")
probabiliteX = probabilite(x, "X")

print()
print("Le Code :")
print("---------")

codeA = codeF(x)

print("")
print("L'Entropie de la source :")
print("-------------------------")

Entropie = entropie(probabiliteX, x, "X")

print("")
print("La Longeur Moyenne du Code R : ")
print("-------------------------------")
R = longeurMoyenne(probabiliteX, x, codeA) 
print("La longeur moyenne du code est : {} Bits/symbole".format(R))

print("")
print("L'Efficacité du Code :")
print("----------------------")
efficacite = round(Entropie/R, 2)

if(Entropie > R):
    print("L'Entropie est supérieure a la longeur moyenne alors le code n'existe pas")
else:
    print("l'efficacité du code est: R = {} Bits/symbole => {}%".format(efficacite, efficacite*100))
    print()    
print()    

