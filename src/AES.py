from Crypto.Cipher import AES
#import binascii as bi
import base64 as b
import os, sys

def decryptage(phrase):
    texte = phrase.encode()
    texte = b.b64decode(texte)
    cle = "YELLOW SUBMARINE"
    texte = decryptage2(texte, cle)
    return texte

def decryptage2(phrase, cle):
    decryptage = AES.new(cle, AES.MODE_ECB)
    texte = decryptage.decrypt(phrase)
    texte = texte.decode()
    return texte

def cryptage(phrase, cle):
    cryptag = AES.new(cle, AES.MODE_ECB)
    texte = bytearray(cryptag.encrypt(phrase))
    return texte

def lecture_fichier():
    with open(os.path.join(sys.path[0],'fichier','aes-in-ecb.txt'), "r") as mon_fichier :
        phrase = mon_fichier.read()
    return phrase

#phrase = lecture_fichier()
#phrase = decryptage(phrase)
#phrase = phrase.decode()
#cle = "YELLOW SUBMARINE"
#print(phrase)
