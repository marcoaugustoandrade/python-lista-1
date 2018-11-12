valor = float(input('Informe o valor da venda: '))

print("Valor com desconto R$ %.2f" % (valor * 0.9))
print("Caso seja parcelado em 3x sem juros, cada parcela será de R$ %.2f" % (valor / 3))
print("A comissão do vendedor caso a venda seja a vista: %.2f" % ((valor * 0.9) * 0.05))
print("A comissão do vendedor caso a venda seja parcelada: %.2f" % (valor * 0.05))
