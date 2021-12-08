def seqNumSom(x, y):
  soma = 0
  for i in range(x, y+1, 1):
    print("{} ".format(i), end="")
    soma = soma + i
  print("Sum={}".format(soma))




x, y = map(int, input().split())

while((x != 0 and y != 0) and (x > 0 and y > 0)):
  if x < y:
    seqNumSom(x, y)
  else:
    seqNumSom(y, x)
  x, y = map(int, input().split())
