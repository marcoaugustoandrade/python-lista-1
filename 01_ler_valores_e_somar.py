# (BACKES, 2012) Faça um programa que solicite ao usuário para digitar três valores inteiros e imprima a soma deles.

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

total = valor1 + valor2 + valor3

# print("A soma dos 3 valores informados é " + str(total))
print("A soma dos 3 valores informados é %s" % total)
