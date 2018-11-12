capacidade_tanque = float(input('Informe a capacidade do tanque (lts): '))
quantidade = float(input('Informe a quantidade de combustível abastecida (lts): '))
quilometragem = float(input('Informe a quilometragem percorrida desde o último abastecimento (km): '))

consumo = quilometragem / (capacidade_tanque - quantidade)

print("O consumo médio do automóvel é de %.2f KM/L" % consumo)
