preco_custo = float(input('Informe o preço de curto do produto: R$ '))
lucro = preco_custo * 0.28
impostos = preco_custo * 0.25

print("O preço final do produto é R$ %.2f" % (preco_custo + lucro + impostos))
