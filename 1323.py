#ENTRADA DE DADOS
while True:
  n = int(input())
#VARIÁVEIS
  soma = 0
#DESENVOLVIMENTO
  if n == 0:
    break
  for i in range(1, n+1, 1):
    soma += i**2
  print(soma)
