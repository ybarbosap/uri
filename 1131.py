cont_grenais = 0
cont_inter = 0
cont_empate = 0
cont_gremio = 0

while True:
    entrada = [int(e) for e in input().split()]
    Inter, Gremio = entrada
    cont_grenais += 1

    if Inter > Gremio:
            cont_inter += 1
    elif Gremio > Inter:
        cont_gremio += 1
    else:
        cont_empate += 1

    grenais = int(input())
    
    if grenais == 2:
        break
    
if cont_inter > cont_gremio:
    resultado = "Inter venceu mais"
elif cont_gremio > cont_inter:
    resultado = "Gremio venceu mais"
else:
    resultado = "Nao houve vencedor"

for e in range(cont_grenais):
    print("Novo grenal (1-sim 2-nao)")
print("{} grenais".format(cont_grenais))
print("Inter:{}".format(cont_inter))
print("Gremio:{}".format(cont_gremio))
print("Empates:{}".format(cont_empate))
print("{}".format(resultado))