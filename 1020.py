dias = int(input())

ano, meses   = divmod(dias, 365)
meses, dias = divmod(meses, 30)


print("{} ano(s)".format(ano))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
