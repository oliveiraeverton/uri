x, y = map(int, input().split())

valor = 1
cont = 0
repetir = 0
while(repetir <= y):
  while(cont < x and valor <= y):
    print(valor, end="")
    
    cont += 1
    valor += 1
    if(cont < x and valor <= y):
      print(end=" ")
  cont = 0
  repetir += x
  if repetir != y:
    print()
