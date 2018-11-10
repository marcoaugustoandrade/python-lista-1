# (BACKES, 2012) Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir  seu objetivo.

import math

altura_degrau = float(input('Informe a altura do degrau (cm): '))
altura_usuario = float(input('Informe a altura que deseja alcançar subindo a escada (cm): '))

print("O usuário deverá subir %d degraus." % (math.ceil(altura_usuario / altura_degrau)))
