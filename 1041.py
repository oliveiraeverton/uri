x, y = map(float, input().split())

if x == 0:
  if y == 0:
    print('Origem')
  else:
    print('Eixo Y')
elif x>0:
  if y>0:
    print('Q1')
  elif y<0:
    print('Q4')
  else:
    print('Eixo X')
else:
  if y<0:
    print('Q3')
  elif y>0:
    print('Q2')
  else:
    print('Eixo X')
