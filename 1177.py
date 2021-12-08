vetor = []

entradaUsuario = int(input())
repetir = 1000
indice = 0
adicionar = 0
while(repetir > 0):
  vetor.append(adicionar)
  adicionar += 1
  if(adicionar == entradaUsuario):
    adicionar = 0
  repetir -= 1
repetir = 1000
while(repetir>0):
  repetir -= 1
  print("N[{}] = {}".format(indice, vetor[indice]))
  indice += 1
