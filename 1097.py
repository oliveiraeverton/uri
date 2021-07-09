i = -1
j = 7
for h in range(5):
  i += 2
  for c in range(3):
    print("I={} J={}".format(i, j))
    j -= 1
  j += 5
