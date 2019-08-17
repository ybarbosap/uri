entrada = [int(e) for e in input().split()]

hi, mi, hf, mf = entrada

horas = hf - hi
minutos = mf - mi

if horas == 0:
    if minutos < 0:
        minutos+=60
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(23, minutos))
    elif minutos == 0:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24, 0))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
elif horas < 0:
    horas += 24
    if minutos < 0:
        minutos += 60
        horas-=1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
else:
    if minutos < 0:
        minutos += 60
        horas -= 1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
