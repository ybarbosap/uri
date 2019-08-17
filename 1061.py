data_inicio = int(input().split()[1])

hora = input().split(":")
hora_inicio = int(hora[0])
minutos_inicio = int(hora[1])
segundos_inicio = int(hora[2])

data_fim = int(input().split()[1])

hora = input().split(":")
hora_fim = int(hora[0])
minutos_fim = int(hora[1])
segundos_fim = int(hora[2])

dias = data_fim - data_inicio 
horas =  hora_fim - hora_inicio
minutos = minutos_fim - minutos_inicio
segundos = segundos_fim - segundos_inicio

if segundos < 0:
    segundos += 60
    minutos -= 1

if minutos < 0:
    minutos += 60
    horas -= 1

if horas < 0:
    horas += 24
    dias -= 1

print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(segundos))
