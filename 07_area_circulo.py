# (BACKES, 2012) Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo e´ π ∗ raio2, considere π = 3.141592.

PI = 3.141592

raio = float(input('Informe o raio do círculo (cm): '))
print("A área do círculo é %.2f cm2" % (PI * (raio ** 2)))
