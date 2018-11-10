# (LIVI & EDELWEISS, 2014) Construa um programa que calcule e informe o consumo médio de combustível de um automóvel. Considere que o tanque é totalmente cheio em cada abastecimento. O programa deve receber, como entradas, a capacidade do tanque, a quantidade de litros abastecidos e a quilometragem percorrida desde o último abastecimento.

capacidade_tanque = float(input('Informe a capacidade do tanque (lts): '))
quantidade = float(input('Informe a quantidade de combustível abastecida (lts): '))
quilometragem = float(input('Informe a quilometragem percorrida desde o último abastecimento (km): '))

consumo = quilometragem / (capacidade_tanque - quantidade)

print("O consumo médio do automóvel é de %.2f KM/L" % consumo)
