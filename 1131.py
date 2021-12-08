somaInter = 0
somaGremio = 0
totalGrenal = 0
empate = 0
novo = 0
while(novo != 2):
  inter, gremio = map(int, input().split())

  totalGrenal += 1
  if inter > gremio:
    somaInter += 1
  elif inter == gremio:
    empate += 1
  else:
    somaGremio +=1
  print("Novo grenal (1-sim 2-nao)")
  novo = int(input())

print('''{} grenais
Inter:{}
Gremio:{}
Empates:{}'''.format(totalGrenal, somaInter, somaGremio, empate))

if somaInter > somaGremio:
  print("Inter venceu mais")
else:
  print("Gremio venceu mais")
