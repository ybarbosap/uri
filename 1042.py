entrada = input().split()
lista = [int(e) for e in entrada]

lista.sort()

print(*lista, sep='\n')
print()
print(*entrada, sep='\n')



