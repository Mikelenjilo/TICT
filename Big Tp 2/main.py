import sys
import codePrefix
import codeShannonFano
import codeHuffman

print("""\n\n\n------------BIG TP 2------------\n
Voici ce que vous pouvez choisir dans ce big tp 2 :  
1 - Code préfix (Vérifier si un code que vous allez introduire est un code préfix ou non).
2 - Code Shannon-Fano (Générer un code avec l'algorithme Shannon-Fano).
3 - Code Huffman (Générer un code avec l'algorithme Shannon-Fanon)
""")
choix = input("Veuiller choisir le nuémro du programme que vous voulez lancer : ")

if(choix == "1"):
    codePrefix.codePrefix()
elif (choix == "2"):
    codeShannonFano.codeShannonFano()
elif (choix == "3"):
    codeHuffman.codeHuffman()
else:
    sys.exit("ERREUR: Vous n'avez pas choisie l'un des options précédentes!")