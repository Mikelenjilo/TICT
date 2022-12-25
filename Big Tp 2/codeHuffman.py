import functions
import math

def codeHuffman():
    code = {}
    tailleDeLaSource = 0
    couple = []
    symboles = []

    print("\n-------------------------------------------------------------------------------------------")
    print("| Bienvenue dans le programme qui permet de générer un code basé sur l'algorithme de Huffman")
    print("--------------------------------------------------------------------------------------------")

    print("\nSaisie de la longeur de la source :")
    print("-----------------------------------")
    tailleDeLaSource = int(input("Donnez la taille de la source : "))

    print("\nSaisie des probabilités et des symboles : ")
    print("------------------------------------------")

    for i in range(tailleDeLaSource):
        symbole = input("Saisissez le symbole {} : ".format(i))
        probabilite = float(input("Saisissez la probablité du symbole \"{}\" : ".format(symbole)))
        couple.append(functions.noeud(probabilite , symbole))
        symboles.append(symbole)

    a = 0

    while(len(couple) > 1):
        for i in range(tailleDeLaSource - 1 - a):
            for j in range(i + 1, tailleDeLaSource - a):
                if(couple[i].probabilite > couple[j].probabilite):
                    couple[i], couple[j] = couple[j], couple[i]

        droite = couple[0]
        gauche = couple[1]

        gauche.code = "0"
        droite.code = "1"

        newCouple = functions.noeud(gauche.probabilite + droite.probabilite, gauche.symbole + droite.symbole, gauche, droite)

        couple.remove(gauche)
        couple.remove(droite)
        couple.append(newCouple)

        a += 1

    codes = functions.generationDuCode(couple[0])

    print("\nLes Codes")
    print("---------")
    for i in range(tailleDeLaSource):
        print("Code de {} \t : {}".format(symboles[i], codes[symboles[i]]))