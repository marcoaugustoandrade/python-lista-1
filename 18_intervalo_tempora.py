# (LIVI & EDELWEISS, 2014) Escreva um programa que transforme o correspondente a um intervalo temporal, expresso em horas, minutos e segundos, no valor correspondente em segundos.

tempo = input('Informe o tempo no formato HH:MM:SS ')
horas = int(tempo[0] + tempo[1])
minutos = int(tempo[3] + tempo[4])
segundos = int(tempo[6] + tempo[7])

print("O tempo correspondente em segundos é %d" % ((horas * 60 * 60) + (minutos * 60) + segundos))
