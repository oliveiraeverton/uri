valorX = int(input())

valorZ = int(input())
while(valorZ <= valorX):
  valorZ = int(input())

quantidadeInteiros = 0
soma = 0
inicio = valorX
while(soma <= valorZ):
  soma += valorX
  valorX += 1
  quantidadeInteiros += 1;

print(quantidadeInteiros)
