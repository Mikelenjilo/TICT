import sys
import math

class node :
	def __init__(self) -> None:
		self.sym=''
		self.pro=0.0
		self.codeLen= 0
		self.arr=[0]*20
		self.top=0
p=[node() for _ in range(20)]

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
	print("\n\n\n\tSymbol\tProbability\tCode",end='')
	for i in range(n - 1,-1,-1):
		print("\n\t", p[i].sym, "\t\t", p[i].pro,"\t"," ",p[i].top+1, " bit(s)  ",end='')
		for j in range(p[i].top+1):
			print(p[i].arr[j],end='')
        
	
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
             sys.exit("Error: The Somme of all probabilities can't be greater than 1")
     elif(a == 1):
         # Vérifie que la somme des probabiltés égale a 1 a la fin de la saisie.
         if(somme != 1):
             sys.exit("Error: The Somme of all probabilities must be equal to 1")
        
def entropie(p, n, name):
    entropie = 0

    for i in range(n):
        entropie += round((p[i].pro * math.log2(1/p[i].pro)), 2)
    
    print("Entropie H({}) = {} Bits/symbole".format(name, entropie))
    
    return entropie

def longeurMoyenne(p, n):
    R = 0

    for i in range(n):
        R += round( (p[i].top+1) * p[i].pro, 2)

    print("Longeur moyenne R  = {} Bits/symbole".format( R))
    return R

if __name__ == '__main__':
	total = 0

	print("Enter number of symbols\t: ",end='')
	n = int(input(""))
	i=0
	for i in range(n):
		print("Enter symbol", i + 1," : ",end="")
		ch = chr(65 + i)
		print(ch)

		p[i].sym += ch
	

	x = probabilite(n, 'X')

	for i in range(n):
		print("\nEnter probability of", p[i].sym, ": ",end="")

		p[i].pro = x[i]
		total = total + p[i].pro

		if (total > 1) :
			print("Invalid. Enter new values")
			total = total - p[i].pro
			i-=1
		
	
	i+=1
	p[i].pro = 1 - total
	sortByProbability(n, p)

	for i in range(n):
		p[i].top = -1

	shannon(0, n - 1, p)

	display(n, p)
 
print("")

Entropie = entropie(p, n, "X")
print("") 

R = longeurMoyenne(p,n)
  
print("") 

print("Efficacite =", round((Entropie / R),2))