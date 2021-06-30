#ENTRADA DE DADOS
a, b, c, d = map(int, input().split())
#PROCESSAMENTO 1
if c>=0 and d>=0 and a%2==0 and c+d>a+b and b>c and d>a:
  print('Valores aceitos')
else:
  print('Valores não aceitos')
