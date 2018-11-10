# (Python.org.br) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
n3 = float(input('Informe um número real: '))

print("%d" % ((n1 * 2) + (n2 / 2)))
print("%.2f" % (3 * n1 + n3))
print("%.2f" % (n3 ** 3))
