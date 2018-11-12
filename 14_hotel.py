import math

diaria = float(input('Informe o valor da diária:'))

print("Diária promocional: R$ %.2f" % (diaria - 25.00))
ocupacao80 = (diaria - 25) * math.ceil(75 * 0.8)
print("Total arrecadado com 80%% de ocupação e diária promocional: R$ %.2f" % ocupacao80)
ocupacao50 = diaria * math.ceil(75 * 0.5)
print("Total arrecadado com 50%% de ocupação e diária promocional: R$ %.2f" % ocupacao50)
print("A diferença é de R$ %.2f" % (ocupacao80 - ocupacao50))
