#1017

#ENTRADA

tempo_horas = int(input())
velocidade  = int(input())

#CALCULO
#ANÁLISE BIDIMENSIONAL>> SE KM/H * H = KM, então:

distancia_percorrida = velocidade*tempo_horas

#ANÁLISE BIDIMENSIONAL>> SE TEMOS KM e QUEREMOS KM/L, então KM/KM/L = L:

combustivel = distancia_percorrida/12


print('{:.3f}'.format(combustivel))
