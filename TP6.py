
#codage du huffman
import math

def proba(taille_of_source):
    vectorProba = []
    for i in range(taille_of_source):
        val = float(input(f"Donner la probabilité {i + 1}: "))
        g = i + 1
        couple = [val, str(g)]
        vectorProba.append(couple)
    return vectorProba


def vector(vectorProba, taille_of_vector):
    debut_of_search = 1
    for j in range(taille_of_vector - 1):
        max_proba = vectorProba[j][0]
        max_pos = j
        for i in range(debut_of_search, taille_of_vector):
            if max_proba < vectorProba[i][0]:
                max_pos = i
                c = vectorProba[j]
                vectorProba[j] = vectorProba[max_pos]
                vectorProba[max_pos] = c
        debut_of_search += 1
    return vectorProba


def zeros_ones(vectorProba, res, ones, zeros, k):
    if k >= 3:
        if (vectorProba[-1][0] != res[0] and vectorProba[-2][0] != res[0]) or res[0] == vectorProba[-3][0]:
            ones.insert(0, vectorProba[-1][1])
            zeros.insert(0, vectorProba[-2][1])
        elif vectorProba[-2][0] == res[0] :
            zeros.insert(0, f'{res[1]}{res[2]}')
            ones.insert(0, vectorProba[-1][1])

        else:
            ones.insert(0, f'{res[1]}{res[2]}')
            zeros.insert(0, vectorProba[-2][1])
    else:
        zeros.insert(0, vectorProba[-2][1])
        ones.insert(0, vectorProba[-1][1])


def addFin(vectorProba):
    res = []
    s = vectorProba[-1][0] + vectorProba[-2][0]
    ID_avant_dernier = vectorProba[-2][1]
    ID_dernier = vectorProba[-1][1]
    res.append(s)
    res.append(ID_avant_dernier)
    res.append(ID_dernier)
    return res


def supprime(vectorProba):
    vectorProba.pop()
    vectorProba.pop()
    return vectorProba


def ajouter(vectorProba, taille_of_vector, res):
    if res[0] < vectorProba[-1][0]:
        vectorProba.append([res[0], f'{res[1]}{res[2]}'])
        return vectorProba
    else:
        for i in range(0, taille_of_vector):
            if res[0] >= vectorProba[i][0]:
                vectorProba.insert(i, [res[0], f'{res[1]}{res[2]}'])
                return vectorProba


def Gcode (ones, zeros, length, code):
    for i in range(0, length):
        id = ones[i]
        for j in range(0, len(id)):
            code[int(id[j]) - 1 ][1] = code[int(id[j]) - 1][1] + "1"
        id = zeros[i]
        for j in range(0, len(id)):
            code[int(id[j]) - 1][1] = code[int(id[j]) - 1][1] + "0"

    return code

print()
print("Saisie de la taille de la source : ")
print("-----------------------------------")
N = int(input(f'Donnez la taille de la source : '))

print()
print("Saisie des probabilites :")
print("-------------------------")
tab= proba(N)
code = []
for i in range(0, N):
    code.append([tab[i][0], ""])

k = N
res = [0]  
ones = []
zeros = []


while k >= 3:
    tab = vector(tab, k) 
    zeros_ones(tab, res, ones, zeros, k) 
    res = addFin(tab)
    tab= supprime(tab) 
    tab = ajouter(tab, k, res) 
    k = k - 1 
zeros_ones(tab, res, ones, zeros, k)
code = Gcode(ones,zeros,len(ones),code)

print()
print("Affichage des codes :")
print("---------------------")
for i in range(N):
    print(f"Le code  {code[i][0]} est: {code[i][1]}")
Entropie = 0
R = 0
Efficacite = 0
for i in range(N):
   
    Entropie = Entropie +round( (code[i][0] * math.log2(1 / code[i][0])),2)
    R = R +round( (code[i][0] * len(code[i][1])),2)
   
   

Efficacite = Efficacite+ round(((Entropie / R) * 100),2)

print()
print("Affichage de l'Entropie :")
print("-------------------------")
print('H(X)=',Entropie)

print()
print("Affichage de la longeur moyenne :")
print("---------------------------------")
print('la longueur moyenne R=',R)

print()
print("Affichage de l'Éfficacité :")
print("---------------------------")
print("l'éfficacité: n=",Efficacite,'%')