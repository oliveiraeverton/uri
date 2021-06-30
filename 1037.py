#ENTRADA DE UM VALOR QUALQUER.
numero = float(input())


#PROCESSAMENTO.
if numero < 0 or numero>100:
  print("Fora do intervalo")
else:
  if 0<=numero<=25.00001:
    print("Intervalo [0,25]")
  elif 25.00001<numero<=50.0001:
    print("Intervalo (25,50]")
  elif 50.0001<numero<=75.0001:
    print("Intervalo (50,75]")
  else:
    print("Intervalo (75,100]")
