def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def nww(a, b):
    return a*b//nwd(a, b)