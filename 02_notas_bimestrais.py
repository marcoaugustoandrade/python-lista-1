# (Python.org.br) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Infome a nota do 1º bimestre: '))
n2 = float(input('Infome a nota do 2º bimestre: '))
n3 = float(input('Infome a nota do 3º bimestre: '))
n4 = float(input('Infome a nota do 4º bimestre: '))

media = (n1 + n2 + n3 + n4) / 4

print("A média final é %.2f" % media)
