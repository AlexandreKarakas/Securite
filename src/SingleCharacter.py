import SingleByte as S
import FixedXOR as f
import binascii as bi
import os, sys
def ouverture_fichier():
    with open(os.path.join(sys.path[0],'fichier' ,'detecting-singlechar-xor.txt'), "r") as mon_fichier :
        tab = mon_fichier.read()
        tab = tab.split()
        max_score = 0
    for i in tab :
        i = bytearray.fromhex(i)
        for y in range(256):
            b = [y] * len(i)
            phrase = (f.fixedXor(i, b))
            phrase = bi.unhexlify(phrase)
            score = S.calcul_score_phrase(phrase)
            if score > max_score :
                max_score = score
                caractere = chr(y)
                value = phrase
    value = value.decode()
    print(max_score, caractere, value)
ouverture_fichier()