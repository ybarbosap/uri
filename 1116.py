import types
n = int(input())
lista = []

for e in range(n):

    x, y = [int(e) for e in input().split()]

    if y == 0:
        lista.append("divisao impossivel")
    else:
        lista.append(x/y)

for e in lista:
    
    if isinstance(e, float):
        print("{:.1f}".format(e))
    else:
        print(e)
