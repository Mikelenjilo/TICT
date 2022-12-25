# Déclaration des varibles
code = {}
tailleDeLaSource = 0
couple = []
symboles = []

class node:
    def __init__(self, probabilite, symbole, gauche = None, droite = None):
        self.symbole = symbole
        self.probabilite = probabilite
        self.gauche = gauche
        self.droite = droite
        self.code = ''
    
def generationDuCode(node, valeur = ''):
    newVal = valeur + node.code

    if(node.gauche):
        generationDuCode(node.gauche, newVal)
    if(node.droite):
        generationDuCode(node.droite, newVal)

    if(not node.gauche and not node.droite):
        code[node.symbole] = newVal

    return code

print()
print("Saisie de la longeur de la source :")
print("---------------------------------------------------")
tailleDeLaSource = int(input("Donnez la taille de la source : "))

print()
print("Saisie des probabilités et des symboles : ")
print("---------------------------------------------------")

for i in range(tailleDeLaSource):
    symbole = input("Saisissez le symbole {} : ".format(i))
    probabilite = float(input("Saisissez la probablité du symbole \"{}\" : ".format(symbole)))
    couple.append(node(probabilite , symbole))
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

    newCouple = node(gauche.probabilite + droite.probabilite, gauche.symbole + droite.symbole, gauche, droite)

    couple.remove(gauche)
    couple.remove(droite)
    couple.append(newCouple)

    a += 1

codes = generationDuCode(couple[0])

for i in range(tailleDeLaSource):
    print("Code de {} \t : {}".format(symboles[i], codes[symboles[i]]))