entrada = 1
qtd = 0
vetor = []
while(entrada>=0):
      qtd += 1
      entrada = int(input())
      vetor.append(entrada)

print("{:.2f}".format((sum(vetor)+entrada*(-1))/(qtd-1)))
