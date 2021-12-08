n = 100
memoria = 0
memoriaPosicao = 0
posicao = 0
while(n > 0):
  n -= 1
  x = int(input())
  posicao += 1
  if(x > memoria):
    memoria = x
    memoriaPosicao = posicao

print(memoria)
print(memoriaPosicao)
