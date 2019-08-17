n = int(input())
valores = []

for e in range(n):
    entrada = [int(e) for e in input().split()]
    x, y = entrada
    soma = 0
    
    if x > y:
        x, y = y, x

    for e in range(x+1,y):
        
        if e % 2 != 0:
            soma += e

    valores.append(soma) 

for e in valores:
    print(e)
