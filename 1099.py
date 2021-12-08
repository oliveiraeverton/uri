def somaImpares(a, b):
    soma = 0
    a += 1
    while a<b:
        if (a%2 == 0):
            a += 1
        else:
            soma += a
            a += 1
    return soma        
n = int(input())       
while(n>0):
  x, y = map(int, input().split())
  if x < y:
      x = somaImpares(x, y)
  else:
      x = somaImpares(y, x)

  print(x)
  n -= 1
