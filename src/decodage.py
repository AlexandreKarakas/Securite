import os, sys
import base64 as b
import binascii
def lecture_fichier():
    with open(os.path.join(sys.path[0],'fichier','fichier.txt'), "r") as mon_fichier :
        contenu = mon_fichier.read()
        print(contenu)
        contenu = binascii.unhexlify(contenu)
        print(contenu)
        contenu = b.b64encode(contenu)
        print(contenu)
        
lecture_fichier()