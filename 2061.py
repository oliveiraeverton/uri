#ENTRADA DE DADOS
numero_abas, acoes = map(int, input().split())

while acoes>0:
  mouse = input()
  acoes -= 1
  if mouse == "fechou":
    numero_abas += 1
  else:
    numero_abas -= 1
print(numero_abas)
