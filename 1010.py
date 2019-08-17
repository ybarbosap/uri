dados1 = input()
dados2 = input()

lista1 = dados1.split()
lista2 = dados2.split()

valor1 = int(lista1[1])
quantidade1 = float(lista1[2])

valor2 = float(lista2[1])
quantidade2 = float(lista2[2])

total = (quantidade1 * valor1) + (quantidade2 * valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))

# 13 2 15.30
# 161 4 5.20