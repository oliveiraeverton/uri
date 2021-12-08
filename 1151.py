def imprimeFib(n):
  a = 0
  b = 1
  if n == 1:
    print(a, end="")
  elif n == 2:
    print(a, end = " ")
    print(b, end = "")
  else:
    print(a, end = " ")
    print(b, end = " ")
    n = n - 2
    while(n>0):
      n -= 1
      soma = a + b
      a = b
      b = soma
      print(soma, end="")
      if n > 0:
          print(end=" ")
quantidadeElementos = int(input())
imprimeFib(quantidadeElementos)
print()
