entrada = [int(e) for e in input().split()]
inicio, fim = entrada

duracao = fim - inicio

if duracao < 0 :
    duracao += 24

if duracao == 0:
    duracao += 24

print("O JOGO DUROU {} HORA(S)".format(duracao))