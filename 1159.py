x = int(input())

while(x != 0):
  soma = 0
  if(x % 2 != 0):
    x += 1
  for i in range(x, x+10, 2):
    soma += x
    x += 2
  print(soma)
  x = int(input())
