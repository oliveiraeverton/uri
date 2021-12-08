casosTeste = int(input())

while(casosTeste>0):
  entradaX, entradaY = map(int, input().split())
  casosTeste -= 1
  soma = 0
  if (entradaX % 2 == 0):
      entradaX += 1
  while(entradaY>0):
    
    soma += entradaX
    entradaX += 2
    entradaY -= 1
  print(soma)  
