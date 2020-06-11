import FixedXOR as f
import AES as a
import PKCS7 as p 
import textwrap as t
import base64 as b
import binascii
import os, sys

def cbc_dechiffrage(s1, cle, IV):
    valeur = a.cryptage(s1, cle)
    cipher = f.fixedXor(valeur, IV)
    return cipher

def cbc_chiffrage(s1, cle, IV):
    texte = p.padding(s1, a.AES.block_size)
    cipher = f.fixedXor(texte, IV)
    valeur = a.cryptage(cipher, cle)
    return valeur

def lecture():
     with open(os.path.join(sys.path[0],'fichier','cbc-mode.txt'), "r") as mon_fichier :
        return mon_fichier.read()


fichier = lecture()
fichier = b.b64decode(fichier)
cle = p.padding("YELLOW SUBMARINE", a.AES.block_size)
IV = (chr(0)).encode()*len(cle)
y = 0
for i in range(a.AES.block_size, len(fichier), a.AES.block_size):
    phrase = fichier[y : i]
    phrase_dechiffrer = cbc_dechiffrage(phrase, cle, IV)
    y = i
    IV = fichier
    phrase_dechiffrer = binascii.unhexlify(phrase_dechiffrer)
    print(phrase_dechiffrer)

