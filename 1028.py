def mdc(valor1, valor2):
  while True:
    resto = valor1 % valor2
    if resto == 0:
      print(valor2)
      break
    valor1 = valor2
    valor2 = resto

  
#ENTRADA DE DADOS
casos_de_testes = int(input())

while casos_de_testes > 0:
  casos_de_testes -= 1
  valor_1, valor_2 = map(int, input().split())
  mdc(valor_1, valor_2)
