# (BACKES, 2012) Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

temperatura = float(input('Informe a temperura (ºC): '))
print("A temperatura em K é: %.2f ºK" % (temperatura + 273.15))
