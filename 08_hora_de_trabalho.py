# (BACKES, 2012) Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

hora_trabalho = float(input('Informe o valor da hora de trabalho: R$ '))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
print("O valor a ser pago ao funcionário é de R$ %.2f" % ((hora_trabalho * horas_trabalhadas) * 1.1))
