#ENTRADA DO CÓDIGO DO PRODUTO:
codigo, quantidade = map(int, input().split())


if codigo == 1:
  #CACHORRO QUENTE
  valor = 4.00*quantidade
elif codigo == 2:
  #X-SALADA
  valor = 4.50*quantidade
elif codigo == 3:
  #X-BACON
  valor = 5.00*quantidade
elif codigo == 4:
  #TORRADA SIMPLES
  valor = 2.00*quantidade
else:
  #REFRIGERANTE
  valor = 1.50*quantidade


print("Total: R$ {:.2f}".format(valor))
