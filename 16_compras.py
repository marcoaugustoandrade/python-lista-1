# (LIVI & EDELWEISS, 2014) Construa um programa que receba os valores (em reais) que cinco clientes pagaram por suas compras. O programa deverá informar o valor da compra média efetuada.

cliente1 = float(input('Informe o valor da compra do 1º cliente: R$ '))
cliente2 = float(input('Informe o valor da compra do 2º cliente: R$ '))
cliente3 = float(input('Informe o valor da compra do 3º cliente: R$ '))
cliente4 = float(input('Informe o valor da compra do 4º cliente: R$ '))
cliente5 = float(input('Informe o valor da compra do 5º cliente: R$ '))

print("O valor médio da compras foi de R$ %.2f" % ((cliente1 + cliente2 + cliente3 + cliente4 + cliente5) / 5))
