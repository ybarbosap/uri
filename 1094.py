n = int(input())

total, C, R, S = 0,0,0,0

for e in range(n):

    quantidade, tipo = input().split()
    str(tipo)
    total += quantidade

    if tipo == "C":
        C += int(quantidade)
    elif tipo == "R":
        R += int(quantidade)
    elif tipo == "S":
        S += int(quantidade)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {(C/total)*100:.2f} %")
print(f"Percentual de ratos: {(R/total)*100:.2f} %")
print(f"Percentual de sapos: {(S/total)*100:.2f} %")