
def padding(s1, t1):
    
    taille = len(s1)
    taillePad = t1 - (taille%t1)
    if taillePad == 0:
        taillePad = t1
    pad = bytes(chr(taillePad), 'utf-8')
    s1 = bytes(s1, 'utf-8')
    return s1 + pad*taillePad



#texte = "YELLOW SUBMARINE"
#texte = padding(texte, 20)
#print(texte)