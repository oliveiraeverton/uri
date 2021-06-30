#ENTRADA DOS VALORES DOS COEFICIENTES DA EQUAÇÃO DO SEGUNDO GRAU
a, b, c = map(float, input().split())

#CALCULANDO O DELTA
delta = b**2 - 4 * a * c

#SE DELTA MENOR DO QUE ZERO, É IMPOSSÍVEL CALCULAR, CASO CONTRÁRIO CONTINUA
if delta<0 or a==0:
  print("Impossivel calcular")
else:
  r1 = (-b + (delta**(1/2)))/(2*a)
  r2 = (-b - (delta**(1/2)))/(2*a)
  print('R1 = {:.5f}'.format(r1))
  print('R2 = {:.5f}'.format(r2))
