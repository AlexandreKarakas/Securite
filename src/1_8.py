from textwrap import wrap
import os, sys
def dictionnaire_valeur(s1):
    chaine = wrap(s1, 16)
    tab = dict()
    for i in chaine:
        tab[i] = 0
    for i in chaine :
        tab[i] = tab[i] + 1
    return tab

def decryptage () :
    with open(os.path.join(sys.path[0],'fichier','detect-aes-ecb.txt'), "r") as mon_fichier :
        texte = mon_fichier.read()
        tab = dictionnaire_valeur(texte)
        print(tab)

decryptage()