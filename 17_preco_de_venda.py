# (LIVI & EDELWEISS, 2014) Um produto comprado por um consumidor tem um preço composto pelo seu preço de custo (preço que a loja paga para a fábrica) adicionado de um percentual de lucro para a loja, além de um percentual de impostos que a loja deve pagar. Supondo que o percentual de lucro seja de 28% do preço de custo e que os impostos sejam de 25% sobre o preço de custo, escreva um algoritmo que calcule o preço que um consumidor deve pagar. O algoritmo deve receber somente o preço de custo de um produto.

preco_custo = float(input('Informe o preço de curto do produto: R$ '))
lucro = preco_custo * 0.28
impostos = preco_custo * 0.25

print("O preço final do produto é R$ %.2f" % (preco_custo + lucro + impostos))
