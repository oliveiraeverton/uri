lista = list(map(int, input().split()))
#função sorted ordena em ordem crescente, se quiser a ordem decrescente adicione no parâmetro reverse=True, ela não altera a lista, atribua ela em uma nova variável.
lista_ordenada = sorted(lista)

for i in lista_ordenada:
  print(i)
print()
for i in lista:
  print(i)
