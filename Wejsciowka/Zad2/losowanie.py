import random

def wylosuj(x):
    tablicaLiczb = []
    i = 0
    while i < x:
        liczba = random.randint(1, 49)
        if(liczba in tablicaLiczb):
            continue
        else:
            tablicaLiczb.append(liczba)
            i+=1
    tablicaLiczb.sort()
    return tablicaLiczb