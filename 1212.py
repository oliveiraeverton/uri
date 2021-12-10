def carrys(x, y, z):
  #z é o restanteMaior
  #variavel
  resultado = 0
  carry = 0
  subiu = False
  if(z == 0):
    #então os números possuem o mesmo tamanho
    #não é necessário utilizar o restanteMaior
    #variavel de controle
    i = len(x)
    while(i>0):
      if(not subiu):
        resultado = int(x[i-1])+int(y[i-1])
      else:
        resultado = int(x[i-1])+int(y[i-1]) + 1
        subiu = False
      if(resultado>=10):
        carry += 1
        subiu = True
      i -= 1
  else:
    #então os números possuem tamanho diferente
    #será necessário urilizar o restanteMaior
    i = len(x)
    while(i>0):
      if(not subiu):
        resultado = int(x[i-1])+int(y[i-1])
      else:
        resultado = int(x[i-1])+int(y[i-1]) + 1
        subiu = False
      if(resultado>=10):
        carry += 1
        subiu = True
      i -= 1
    #ainda falta o RestanteMaior
    i = len(z)
    while(i>0):
      #resultado = int(resultado) + int(z[i-1])
      if(resultado>=10):
        resultado = 1 + int(z[i-1])
        if(resultado>=10):
          carry += 1
      else:
        break
      i -= 1
  
  if(carry > 1):
    print("{} carry operations.".format(carry))
  elif(carry == 1):
    print("{} carry operation.".format(carry))
  else:
    print("No carry operation.")

def main():
  entradaX, entradaY = map(str, input().split())
  while(entradaX != "0" or entradaY != "0"):

    maior = len(entradaX)
    menor = len(entradaY)

    #Variaveis Globais
    carry = 0

    if(maior == menor):
      restanteMaior = 0

    elif(maior>menor):
      restanteMaior = entradaX[:-(len(entradaY))]
      entradaX = entradaX[-(len(entradaY)):]
      #entradaY = entradaY[:] já é a menor parte
    else:
      restanteMaior = entradaY[:-(len(entradaX))]
      #entradaX = entradaX[:] já é a menor parte
      entradaY = entradaY[-(len(entradaX)):]

    carrys(entradaX, entradaY, restanteMaior)
    entradaX, entradaY = map(str, input().split())
main()
