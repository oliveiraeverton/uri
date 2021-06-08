#1050


ddd = int(input())

lista = [11, 19, 21, 27, 31, 32, 61, 71]
nome = ['Sao Paulo', 'Campinas', 'Rio de Janeiro', 'Vitoria', 'Belo Horizonte', 'Juiz de Fora',
        'Brasilia', 'Salvador',]


if ddd in lista:
    for i in range(0, len(lista), 1):
      if ddd == lista[i]:
        print(nome[i])

else:
  print("DDD não cadastrado")
