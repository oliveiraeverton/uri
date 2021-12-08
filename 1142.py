entrada = int(input())

valor = 1

while(entrada > 0):
  entrada -= 1
  for i in range(1, 4, 1):
    print("{} ".format(valor), end="")
    valor += 1
  valor += 1
  print("PUM")
