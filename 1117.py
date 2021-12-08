def validaNota(x):
  if x < 0 or x > 10:
    print("nota invalida")
    x = float(input())
    x = validaNota(x)
  return x

nota1 = float(input())
nota1 = validaNota(nota1)
nota2 = float(input())
nota2 = validaNota(nota2)

print("media = {:.2f}".format((nota1+nota2)/2))
