# (LIVI & EDELWEISS, 2014) Um hotel com 75 apartamentos deseja fazer uma promoção especial de final de semana, concedendo um desconto de R$ 25,00 na diária. Com isso, espera aumentar sua taxa de ocupação de 50 para 80%. Sendo dado o valor normal da diária, calcule e imprima:
# O valor da diária promocional;
# O valor total arrecadado com 80% de ocupação e diária promocional;
# O valor total arrecadado com 50% de ocupação e diária normal;
# A diferença entre esses dois valores;

import math

diaria = float(input('Informe o valor da diária:'))

print("Diária promocional: R$ %.2f" % (diaria - 25.00))
ocupacao80 = (diaria - 25) * math.ceil(75 * 0.8)
print("Total arrecadado com 80%% de ocupação e diária promocional: R$ %.2f" % ocupacao80)
ocupacao50 = diaria * math.ceil(75 * 0.5)
print("Total arrecadado com 50%% de ocupação e diária promocional: R$ %.2f" % ocupacao50)
print("A diferença é de R$ %.2f" % (ocupacao80 - ocupacao50))
