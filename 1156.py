#S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

#primos/1+1


baixo = 1
soma = 1
cima = 3
while(cima<39):
  baixo += baixo
  soma += cima/baixo
  cima += 2
  
print("{:.2f}".format(soma))
