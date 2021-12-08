n = int(input())

while(n>0):
  x, y, z = map(float, input().split())
  media = ((x*2)+(y*3)+(z*5))/10
  print("{:.1f}".format(media))
  n -= 1
