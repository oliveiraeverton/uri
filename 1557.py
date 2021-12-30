n = int(input())
while(n != 0):
  matriz = []


  #preenchendo a primeira linha da matriz
  lista = []
  lista.append(1)
  for i in range(1, n):
    calculo = 2 ** i
    lista.append(calculo)

  matriz.append(lista)

  for i in range(1, n):
    lista = []
    for j in range(0, n):
      if (j == 0):
        lista.append(matriz[i-1][1])
      else:
        calculo = matriz[i-1][j] * 2
        lista.append(calculo)
    matriz.append(lista)

  ultimoElemento = len(str(matriz[n-1][n-1]))

  for i in range(0, n, 1):
    for j in range(0, n, 1):
      if(j==n-1):
        print("{:>{}d}".format(matriz[i][j], ultimoElemento), end = "")
      else:
        print("{:>{}d}".format(matriz[i][j], ultimoElemento), end = " ")
    print()
  print()
  n = int(input())
