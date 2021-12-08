casosTeste = int(input())

cidadeA = 0
cidadeB = 0
crescimentoA = 0
crescimentoB = 0

cont = 0
while(casosTeste > 0):
  casosTeste -= 1
  cidadeA, cidadeB, crescimentoA, crescimentoB = map(float, input().split())
  crescimentoA = crescimentoA/100
  crescimentoB = crescimentoB/100
  while((cidadeA <= cidadeB and cont <= 100)):
    
    cont += 1
    cidadeA += int(cidadeA*crescimentoA)
    cidadeB += int(cidadeB*crescimentoB)
  if(cont > 100):
    print("Mais de 1 seculo.")
  else:
    print(cont,"anos.")
  cont = 0
