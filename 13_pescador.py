peso = float(input('Informe o peso: '))
excesso = peso - 50
multa = excesso * 4.00

print("Foram excedidos %.2f KG, definindo uma multa de R$ %.2f" % (excesso, multa))
