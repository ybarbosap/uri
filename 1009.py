nome = input()
sfixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
salario = sfixo + comissao
print('TOTAL = R${:.2f}'.format(salario))