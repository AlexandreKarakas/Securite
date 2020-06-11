import os

def random_key(taille): 
    random_Key = os.urandom(taille)
    return random_Key
