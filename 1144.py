entrada = int(input())

n = 1
while(entrada > 0):
  print("{} {} {}".format(n, n**2, n**3))
  print("{} {} {}".format(n, n**2+1, n**3+1))
  entrada -= 1
  n += 1
