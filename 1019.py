#1019

segundos = int(input())

horas, resto = divmod(segundos, 3600)
minutos, segundos = divmod(resto, 60)


print("{}:{}:{}".format(horas, minutos, segundos))
