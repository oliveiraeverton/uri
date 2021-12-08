#S = 1 + 1/2 + 1/3 + … + 1/100

indice = 2

soma = 1
repeticao = 99
while(repeticao > 0):
  soma += 1/indice;
  indice += 1
  repeticao -= 1
print("{:.2f}".format(soma))
