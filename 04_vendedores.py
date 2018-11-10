# (BACKES, 2012) Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# o total a pagar com desconto de 10%;
# o valor de cada parcela, no parcelamento de 3× sem juros;
# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total) ;

valor = float(input('Informe o valor da venda: '))

print("Valor com desconto R$ %.2f" % (valor * 0.9))
print("Caso seja parcelado em 3x sem juros, cada parcela será de R$ %.2f" % (valor / 3))
print("A comissão do vendedor caso a venda seja a vista: %.2f" % ((valor * 0.9) * 0.05))
print("A comissão do vendedor caso a venda seja parcelada: %.2f" % (valor * 0.05))
