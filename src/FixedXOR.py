import binascii as bi

def str_hex(str):
    return int(str, base=16)


def fixedXor(s1, s2) :
    tab = bytes(a^b for (a, b) in zip(s1, s2))
    tab = bi.hexlify(tab)
    return tab

def fixedXOR2(s1, s2):
    value = hex(int(s1, 16)^(int(s2, 16)))
    return value

#s1 = ("1c0111001f010100061a024b53535009181c")
#s2 = ("686974207468652062756c6c277320657965")

#s = fixedXOR2(s1, s2)
#print(s[2:])