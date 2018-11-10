# (BACKES, 2012) Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.

velocidade = float(input('Informe a velocidade (km/h): '))
print("A velocidade em m/s é %.2f" % (velocidade / 3.6))
