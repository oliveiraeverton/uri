entradaG = -1

entradaG = list(input().split())

valorA = entradaG[0]
valorN = entradaG[len(entradaG)-1]

valorA = int(valorA)
valorN = int(valorN)
i = 0
soma = 0
while(valorN>0):
  soma = valorA + i + soma
  valorN -= 1
  i += 1
print(soma)
