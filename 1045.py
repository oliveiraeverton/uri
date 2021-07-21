#ENTRADA DE VALORES
lista = list(map(float, input().split()))
#ORGANIZANDO A LISTA PARA QUE O PRIMEIRO ELEMENTO SEJA O MAIOR VALOR
lista.sort(reverse=True)

a, b, c = lista[0], lista[1], lista[2]

if a >= b+c:
  print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
  print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
  print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
  print("TRIANGULO ACUTANGULO")
if a == b == c:
  print("TRIANGULO EQUILATERO")
elif a==b or b==c or a==c:
  print("TRIANGULO ISOSCELES")
