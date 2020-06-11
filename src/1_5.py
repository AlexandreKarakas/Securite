import FixedXOR as f
import os, sys
def cryptage():
     with open(os.path.join(sys.path[0],'fichier','ICE.txt'), "r") as mon_fichier :
        phrase = mon_fichier.read()
        phrase = phrase.encode()
        b = bytes("ICE" * len(phrase), 'utf-8')
        crypt = f.fixedXor(phrase, b)
        crypt = crypt.decode()
        print(crypt)

cryptage()