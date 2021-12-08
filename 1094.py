casosTeste = int(input())
sapo = 0
rato = 0
coelho = 0
total = 0
while(casosTeste > 0):
  casosTeste -= 1
  entradaInteira, siglaString = map(str, input().split(" "))
  total += int(entradaInteira)
  if siglaString == "C":
    coelho += int(entradaInteira)
  elif siglaString == "R":
    rato += int(entradaInteira)
  else:
    sapo += int(entradaInteira)

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))
print("Percentual de coelhos: {:.2f} %".format((coelho/total)*100))
print("Percentual de ratos: {:.2f} %".format((rato/total)*100))
print("Percentual de sapos: {:.2f} %".format((sapo/total)*100))
