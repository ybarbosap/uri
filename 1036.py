entrada = [float(e) for e in (input().split())]
A, B, C = entrada

if A == 0:
    print("Impossivel calcular")
else:
    discriminante = ((B**2) - (4*A*C))
    if discriminante > 0:
        discriminante = discriminante ** (1/2)
        R1 = ((-B) + discriminante)/(2*A)
        R2 = ((-B) - discriminante)/(2*A)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))
    else:
        print("Impossivel calcular")
        