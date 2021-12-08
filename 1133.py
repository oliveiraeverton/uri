def decideImpressao(x, y):
  x += 1
  while(x<y):
    if(x%5 == 2 or x%5 == 3):
      print(x)
    x += 1


x = int(input())
y = int(input())
if(x < y):
  decideImpressao(x, y)
else:
  decideImpressao(y, x)
