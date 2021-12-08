def divisao(x, y):
  if y == 0:
    print("divisao impossivel")
  else:
    print("{:.1f}".format(x/y))

casosTeste = int(input())

while(casosTeste > 0):
  x, y = map(int, input().split())
  divisao(x,y)
  casosTeste -= 1
