#2949
n = int(input()) #0< n <=10

i = 0
a = 0 #anao
e = 0 #elfo
h = 0 #humano
m = 0 #mago
x = 0 #hobbit
while i<n:
  b = input()
  b = b[-1]
  i = i + 1
  if b=='X':
    x = x + 1
  if b=='M':
    m = m + 1
  if b=='H':
    h = h + 1
  if b=='E':
    e = e + 1
  if b=='A':
    a = a + 1

print('{} Hobbit(s)'.format(x))
print('{} Humano(s)'.format(h))
print('{} Elfo(s)'.format(e))
print('{} Anao(s)'.format(a))
print('{} Mago(s)'.format(m))
