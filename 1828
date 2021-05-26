#1828

#funções
def bazinga(a):
  print('Caso #{}: Bazinga!'.format(a))
  
def raj(a):
  print('Caso #{}: Raj trapaceou!'.format(a))

#qtd de testes
t = int(input())
a = 1
#CONDIÇÕES
while t>0:
  jogo1, jogo2 = input().split()
  if jogo1 == jogo2:
    print('Caso #{}: De novo!'.format(a))
  else:
    if jogo1 == 'lagarto':
      if jogo2 == 'Spock' or jogo2 == 'papel':
        bazinga(a)
      else:
        raj(a)
    elif jogo1 == 'Spock':
      if jogo2 == 'tesoura' or jogo2 == 'pedra':
        bazinga(a)
      else:
        raj(a)
    elif jogo1 == 'papel':
      if jogo2 == 'pedra' or jogo2 == 'Spock':
        bazinga(a)
      else:
        raj(a)
    elif jogo1 == 'tesoura':
      if jogo2 == 'papel' or jogo2 == 'lagarto':
        bazinga(a)
      else:
        raj(a)
    elif jogo1 == 'pedra':
      if jogo2 == 'lagarto' or jogo2 == 'tesoura':
        bazinga(a)
      else:
        raj(a)
  a = a + 1
  t = t - 1
