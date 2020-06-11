import FixedXOR as f
import binascii as bi

def charger_dictionnaire() :
    frequence = dict()
    #dictionnaire de frequence sur 40 000 mots en anglais
    frequence['A'] = 8.08
    frequence['a'] = 8.08
    frequence['B'] = 1.67
    frequence['b'] = 1.67
    frequence['C'] = 3.18
    frequence['c'] = 3.18
    frequence['D'] = 3.99
    frequence['d'] = 3.99
    frequence['E'] = 12.56
    frequence['e'] = 12.56
    frequence['F'] = 2.17
    frequence['f'] = 2.17
    frequence['G'] = 1.80
    frequence['g'] = 1.80
    frequence['H'] = 5.27
    frequence['h'] = 5.27
    frequence['I'] = 7.24
    frequence['i'] = 7.24
    frequence['J'] = 0.14
    frequence['j'] = 0.14
    frequence['K'] = 0.63
    frequence['k'] = 0.63
    frequence['M'] = 2.60
    frequence['m'] = 2.60
    frequence['N'] = 7.38
    frequence['n'] = 7.38
    frequence['O'] = 7.47
    frequence['o'] = 7.47
    frequence['P'] = 1.91
    frequence['p'] = 1.91
    frequence['Q'] = 0.09
    frequence['q'] = 0.09
    frequence['R'] = 6.42
    frequence['r'] = 6.42
    frequence['S'] = 6.59
    frequence['s'] = 6.59
    frequence['T'] = 9.15
    frequence['t'] = 9.15
    frequence['U'] = 2.79
    frequence['u'] = 2.79
    frequence['V'] = 1.00
    frequence['v'] = 1.00
    frequence['W'] = 1.89
    frequence['w'] = 1.89
    frequence['X'] = 0.21
    frequence['x'] = 0.21
    frequence['Y'] = 1.65
    frequence['y'] = 1.65
    frequence['Z'] = 0.07
    frequence['z'] = 0.07
    frequence[' '] = 2.0
    return frequence


def score(c):
    alphabet = charger_dictionnaire()
    value = 0
    if c in alphabet :
        value  = alphabet.get(c)
    return value

def calcul_score_phrase(s1):
    alphabet = charger_dictionnaire()
    score_value = 0
    for i in s1 :
        p = chr(i)
        score_value = score_value + score(p)
    return score_value

def dechiffrement_xor(s1) :
    list_max = 0
    caractere = None
    b = list()
    alphabet = charger_dictionnaire()
    for i in alphabet.keys() :
        b = [ord(i)] * len(s1)
        phrase = (f.fixedXor(s1, b))
        phrase = bi.unhexlify(phrase)
        max_score = calcul_score_phrase(phrase)
        if max_score > list_max :
            list_max = max_score
            caractere = i
    b = [ord(caractere)] * len(s1)
    phrase = (f.fixedXor(s1, b))
    phrase = bi.unhexlify(phrase)
    return caractere, list_max

    

s1 = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
dechiffrement_xor(s1)
