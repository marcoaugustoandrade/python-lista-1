import math

area = float(input('Informe o tamanho da área a ser pintada (m2): '))
qtd_necessaria = area / 6
lata_18 = math.ceil(qtd_necessaria / 18)
galoes_36 = math.ceil(qtd_necessaria / 3.6)

print("Utilizando latas de 18 litros você precisa de %.0f latas de 18 litros, totalizando R$ %.2f" % (lata_18, (lata_18 * 80.00)))
print("Utilizando latas de 3,6 litros você precisa de %.0f latas de 3,6 litros, totalizando R$ %.2f" % (galoes_36, (galoes_36 * 25.00)))
