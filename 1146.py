entrada = int(input())
i = 1
while(entrada!=0):
  
  while(entrada>0):
    
    print(i, end="")
    if(entrada-1 > 0):
      print(end=" ")
    entrada -= 1
    i += 1
  
  print()
  i = 1
  entrada = int(input())
