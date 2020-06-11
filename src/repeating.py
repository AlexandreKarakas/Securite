import FixedXOR as f

def distance_hamming(s1, s2) :
    resultat = 0
    a = bytearray(s1, 'utf-8')
    b = bytearray(s2, 'utf-8')
    c = f.fixedXor(a, b)
    taille = len(s1)
    for i in range(taille) :
        if (caractere(s1, i) != caractere(s2, i)) :
            resultat = resultat + 1
    return resultat

def caractere(s1, index) :
    return s1[index]

s1 = "this is a test"
s2 = "wokka wokka!!!"

valeur = distance_hamming(s1, s2)
print(valeur)