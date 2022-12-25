import functions

longeurMoyenne_output = 0.0
code_input = []

def codePrefix():
    print()
    print("---------------------------------------------------------------------------------------------")
    print("|Bienvenue dans le programme qui permet de savoir si un code donné est un code préfix ou non|")
    print("---------------------------------------------------------------------------------------------")

    print()
    print("Saisie de la longeur de la séquence X :")
    print("---------------------------------------")
    x = int(input("Spécifier la longeur de la séquence X : "))

    print()
    print("Saisie des probabilitées de la séquence X :")
    print("--------------------------------------------")
    probabilites_input = functions.probabilite(x, "X")

    print()
    print("Le Code :")
    print("---------")
    code_input = functions.verifie_code_prefix(x)

    print()
    print("L'Entropie de la source :")
    print("-------------------------")
    entropie_output = functions.entropie(probabilites_input, x, "X")

    print()
    print("La Longeur Moyenne du Code R:")
    print("-----------------------------")
    longeurMoyenne_output = functions.longeur_moyenne(probabilites_input, x, code_input)

    print()
    print("L'Efficacité du code :")
    print("----------------------")
    efficacite_output = functions.efficacite(entropie_output, longeurMoyenne_output)

    print()