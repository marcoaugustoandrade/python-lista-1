codigo = int(input('Informe o código do produto: '))
nome = input('Informe o nome do produto: ')
quantidade = float(input('Informe a quantidade do produto: '))
valor_unitario = float(input('Informe o valor unitário: '))

valor_total = quantidade * valor_unitario

print("Foram comprados %.2f unidades do produto %s, com código %d, no valor unitário de R$ %.2f, totalizando R$ %.2f" % (quantidade, nome, codigo, valor_unitario, valor_total))
