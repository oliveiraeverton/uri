#FDME 9
#PÁGINA 55

#EM TODO TRIÂNGULO, CADA LADO É MAIOR QUE A DIFERENÇA DOS OUTROS DOIS.

#SE a, b, c SÃO AS MEDIDAS DOS LADOS DE UM TRIÂNGULO, DEVEMOS TER AS TRÊS CONDIÇÕES ABAIXOS:
# a < b+c
# b < a+c
# c < a+b

#E estas relações podem ser resumidas como:

# |b-c| < a < b + c

#ELEVAR b-c ao quadrado e retirar a raiz, retirará o negativo se for o caso.


a, b, c = map(float, input().split())

modulo = ((b-c)**2)**(1/2)


if modulo < a < b + c: #SE TRUE == É TRIÂNGULO
  print("Perimetro = {:.1f}".format(a+b+c))
else:
  print("Area = {:.1f}".format(((a+b)*c)/2))
