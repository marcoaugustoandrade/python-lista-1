comprimento = float(input('Informe o comprimento do terreno (mts): '))
largura = float(input('Informe a largura do terreno (mts): '))
preco = float(input('Informe o preço do metro de tela: R$ '))

print("O custo para cercar o terreno é de R$ %.2f" % ((comprimento +largura) * preco))
