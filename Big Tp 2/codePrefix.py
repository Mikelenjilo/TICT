import functions

longeurMoyenne_output = 0.0
code_input = []

def codePrefix():
    print("\n-----------------------------------------------------------------------------------------------")
    print("| Bienvenue dans le programme qui permet de savoir si un code donné est un code préfix ou non |")
    print("-----------------------------------------------------------------------------------------------")

    print("\nSaisie de la longeur de la séquence X :")
    print("---------------------------------------")
    x = int(input("Spécifier la longeur de la séquence X : "))

    print("\nSaisie des probabilitées de la séquence X :")
    print("--------------------------------------------")
    probabilites_input = functions.probabilite(x, "X")

    print("\nLe Code :")
    print("---------")
    code_input = functions.verifie_code_prefix(x)

    print("\nL'Entropie de la source :")
    print("-------------------------")
    entropie_output = functions.entropie(probabilites_input, x, "X")

    print("\nLa Longeur Moyenne du Code R:")
    print("-----------------------------")
    longeurMoyenne_output = functions.longeur_moyenne(probabilites_input, x, code_input)

    print("\nL'Efficacité du code :")
    print("----------------------")
    efficacite_output = functions.efficacite(entropie_output, longeurMoyenne_output)
