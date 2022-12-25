import sys
import math

#------------Functions Générales------------
def error_checker(a, somme): # Fonction qui permet de vérifier si il n ya pas d'erreurs dans les probabilitées.
    if(a == 0):
        # Vérifie que la somme des probabiltés ne dépace pas le 1.
        if(somme > 1):
            sys.exit("Erreur : La somme des probabilitées ne peut pas être supérieur a 1")
    elif(a == 1):
        # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
        if(somme != 1):
            sys.exit("Erreur : La somme des probabilitées doit être égale a 1")

def probabilite(n, name): # Fonction qui permet de saisir les probabilitées.
    somme = 0
    probabilites = []

    for i in range(n):
        l = float(input("Spécifier la probabilité P({}{}) = ".format(name, i)))
        probabilites.append(l)
        somme = somme + l
        error_checker(0, somme) # Vérifier que la somme ne dépace pas le 1.
    error_checker(1, somme) # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
    
    return probabilites

def entropie(probabilite, n, name): # Fonction qui permet de calculer l'entropie
    entropie = 0.0
    for i in range(n):
        entropie = round(entropie + (probabilite[i] * math.log2(1/probabilite[i])), 2)
    
    print("Entropie H({}) = {} Bits/symbole".format(name, entropie))
    
    return entropie

def longeur_moyenne(probabilite, n, code):
    longeurMoyenne_output = 0.0
    for i in range(n):
        longeurMoyenne_output = round(longeurMoyenne_output + len(code[i]) * probabilite[i], 2)
    
    print("La longeur moyenne du code est : {} Bits/symbole".format(longeurMoyenne_output))
    
    return longeurMoyenne_output

def efficacite(entropie, longeurMoyenne):
    efficacite_output = 0.0

    if(entropie > longeurMoyenne):
        print("L'entropie est supérieure à la longeur moyenne alors le code n'existe pas")
    else :
        efficacite_output = round(entropie/longeurMoyenne, 4)
        print("L'éfficacité cu code est : {} => {}%".format(efficacite_output, round(efficacite_output * 100, 2)))

    return efficacite_output

#--------------------Code Préfix--------------------
def verifie_code_prefix(n):
    code = []
    a = True

    for i in range(n):
        l = input("Donner le code correspondant qu élémenet n°{} : ".format(i))
        code.append(l)

    for i in range(n):
        for j in range(n):
            if(len(code[i]) < len(code[j])):
                t = code[j]
                code[j] = code[i]
                code[i] = t
    
    for i in range(0, n-1):
        for j in range(i+1, n):
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

#--------------------Code Shannon Fano--------------------
class node:
    def __init__(self) -> None:
        self.sym=''
        self.pro=0.0
        self.codeLen=0
        self.arr=[0]*20
        self.top=0

def shannon(l, h, p):
	pack1 = 0; pack2 = 0; diff1 = 0; diff2 = 0
	if ((l + 1) == h or l == h or l > h) :
		if (l == h or l > h):
			return
		p[h].top+=1
		p[h].arr[(p[h].top)] = 0
		p[l].top+=1
		p[l].arr[(p[l].top)] = 1
		
		return
	
	else :
		for i in range(l,h):
			pack1 = pack1 + p[i].pro
		pack2 = pack2 + p[h].pro
		diff1 = pack1 - pack2
		if (diff1 < 0):
			diff1 = diff1 * -1
		j = 2
		while (j != h - l + 1) : # Tant que ( j != 3)
			k = h - j
			pack1 = pack2 = 0
			for i in range(l, k+1):
				pack1 = pack1 + p[i].pro
			for i in range(h,k,-1):
				pack2 = pack2 + p[i].pro
			diff2 = pack1 - pack2
			if (diff2 < 0):
				diff2 = diff2 * -1
			if (diff2 >= diff1):
				break
			diff1 = diff2
			j+=1
		
		k+=1
		for i in range(l,k+1):
			p[i].top+=1
			p[i].arr[(p[i].top)] = 1
			
		for i in range(k + 1,h+1):
			p[i].top+=1
			p[i].arr[(p[i].top)] = 0
			
		shannon(l, k, p)
		shannon(k + 1, h, p)


def sortByProbability(n, p):
	temp=node()
	for j in range(1,n) :
		for i in range(n - 1) :
			if ((p[i].pro) > (p[i + 1].pro)) :
				temp.pro = p[i].pro
				temp.sym = p[i].sym

				p[i].pro = p[i + 1].pro
				p[i].sym = p[i + 1].sym

				p[i + 1].pro = temp.pro
				p[i + 1].sym = temp.sym
			
		
def display(n, p):
    print("\n\n\tSymbole\tProbabilité\tCode")
    for i in range(n-1, -1, -1):
        print("\n\t", p[i].sym, "\t", p[i].pro, "\t\t", end='')
        for j in range(p[i].top+1):
            print(p[i].arr[j], end='')
    print()

def longeur_moyenne_shanon_fano(p, n):
    R = 0

    for i in range(n):
        R += round( (p[i].top+1) * p[i].pro, 2)

    print("Longeur moyenne R  = {} Bits/symbole".format( R))
    return R

#--------------------Code Huffman--------------------
code = {}
tailleDeLaSource = 0
couple = []
symboles = []

class noeud:
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