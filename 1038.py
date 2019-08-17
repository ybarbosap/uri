data = input()
lista = data.split()

codigo = int(lista[0])
qtt = int(lista[1])

if codigo == 1:
    total = qtt * 4.00
elif codigo == 2:
    total = qtt * 4.50
elif codigo == 3:
    total = qtt * 5.00
elif codigo == 4:
    total = qtt * 2.00
elif codigo == 5:
    total = qtt * 1.50

print('Total: R$ {:.2f}'.format(total))
