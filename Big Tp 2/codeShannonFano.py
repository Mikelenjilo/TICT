import functions

def codeShannonFano():
    i = 0
    n = 0
    total = 0
    a = []
    x = []
    p = [functions.node() for _ in range(20)]

    print("\n-------------------------------------------------------------------------------------------------")
    print("| Bienvenue dans le programme qui permet de générer un code basé sur l'algorithme de Shannon Fano")
    print("-------------------------------------------------------------------------------------------------")

    print("\nSaisie du nombre des symboles :")
    print("-------------------------------")
    n = int(input("Entrer le nombre des symboles : "))

    print("\nSaisie des symboles : ")
    print("----------------------")

    for i in range(n):
        ch = input("Enter le symbole {} : ".format(i))
        p[i].sym = ch

    print("\nSaisie des probabilités :")
    print("-------------------------")
    x = functions.probabilite(n, 'X')

    for i in range(n):
        p[i].pro = x[i] 

    i+=1 # i = n
    p[i].pro = 1 - total
    functions.sortByProbability(n, p)

    for i in range(n):
        p[i].top = -1

    functions.shannon(0, n-1, p)
    functions.display(n, p)

    print("\nEntropie : ")
    print("-----------")
    entropie_output = functions.entropie(x, n, "X")

    print("\nLongeur Moyenne : ")
    print("------------------")
    longeurMoyenne_output =functions.longeur_moyenne_shanon_fano(p, n)

    print("\nEfficacité :")
    print("------------")
    efficacite_output = functions.efficacite(entropie_output, longeurMoyenne_output)