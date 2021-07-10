salario = float(input())
reajuste = salario
if salario <= 400:
  #reajuste de 15%
  salario *= 1.15
  var = "15 %"
elif 400.01 <= salario <= 800:
  #reajuste 12%
  salario *= 1.12
  var = "12 %"
elif 800.01 <= salario <= 1200:
  #reajuste 10%
  salario *= 1.10
  var = "10 %"
elif 1200.01 <= salario <= 2000:
  #reajuste 7%
  salario *= 1.07
  var = "7 %"
else:
  #reajuste 4%
  salario *= 1.04
  var = "4 %"
reajuste = salario - reajuste
print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {}".format(var))
