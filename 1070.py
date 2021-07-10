numero = int(input())

if numero%2 == 0:
  numero += 1 #TORNA O NÚMERO ÍMPAR
  for i in range(6):
    print(numero)
    numero += 2
else:
  for i in range(6):
    print(numero)
    numero += 2
