# (BACKES, 2012) Tres amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

amigo1 = float(input('Informe o valor que o 1º amigo apostou: R$ '))
amigo2 = float(input('Informe o valor que o 2º amigo apostou: R$ '))
amigo3 = float(input('Informe o valor que o 3º amigo apostou: R$ '))
premio = float(input('Informe o valor do prêmio: R$ '))

total_apostado = amigo1 + amigo2 + amigo3

print("O amigo 1 vai ficar com R$ %.2f " % (premio * ((amigo1 * 100 / total_apostado) / 100)))
print("O amigo 2 vai ficar com R$ %.2f " % (premio * ((amigo2 * 100 / total_apostado) / 100)))
print("O amigo 3 vai ficar com R$ %.2f " % (premio * ((amigo3 * 100 / total_apostado) / 100)))
