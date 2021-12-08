casosTeste = int(input())

while(casosTeste>0):
  casosTeste -= 1
  numeroPerfeito = int(input())
  soma = 0
  divisores = 1
  while(numeroPerfeito>divisores):
    if(numeroPerfeito%divisores == 0):
      soma += divisores
    divisores += 1
  if(soma == numeroPerfeito):
    print(numeroPerfeito,"eh perfeito")
  else:
    print(numeroPerfeito,"nao eh perfeito")
