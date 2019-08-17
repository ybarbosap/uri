dados = input()
lista = dados.split()
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

# area = b*a/2
triangulo = (A*C)/2
# circulo = π r²
pi = 3.14159
circulo = pi * C**2
# trapezio = ((B+b)*h)/2
trapezio = ((A + B)*C)/2
aquadrado = B*B
aretangulo = A*B

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(aquadrado))
print('RETANGULO: {:.3f}'.format(aretangulo))