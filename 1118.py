#1118
i = 0
x = 1
while i < 2:
  n = float(input())
  if 0 <= n <= 10:
    while True:
      n2 = float(input())
      if 0 <= n2 <= 10:
        media = (n+n2)/2
        print('media = {:.2f}'.format(media))
        x = 0
        break
      else:
        print('nota invalida')
    while x<1:
      print('novo calculo (1-sim 2-nao)')
      q = int(input())
      if q==1:
        x = x + 1
      elif q<1 or q>2:
        continue
      else:
        i = 2
        break
    #else:
      #print('nota invalida')
  else:
    print('nota invalida')
