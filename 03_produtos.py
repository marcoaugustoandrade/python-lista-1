# (PUGA & RISSETI, 2016) Uma loja de produtos eletrônicos com vendas regulares opta por contratar uma equipe para a organização de um sistema de gerenciamento de vendas. Seu desafio será elaborar um algoritmo que, a partir de dados fornecidos pelo usuário, calcule o valor da venda de um produto, exibindo uma saída em vídeo contendo o código do produto, o nome, a quantidade comprada, o valor unitário e o valor total.

codigo = int(input('Informe o código do produto: '))
nome = input('Informe o nome do produto: ')
quantidade = float(input('Informe a quantidade do produto: '))
valor_unitario = float(input('Informe o valor unitário: '))

valor_total = quantidade * valor_unitario

print("Foram comprados %.2f unidades do produto %s, com código %d, no valor unitário de R$ %.2f, totalizando R$ %.2f" % (quantidade, nome, codigo, valor_unitario, valor_total))
