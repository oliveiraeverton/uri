def somaImpares(a, b):
    soma = 0
    a += 1
    while a<b:
        if (a%2 == 0):
            a += 1
        else:
            soma += a
            a += 1
    return soma        
        
x = int(input())
y = int(input())



if x < y:
    x = somaImpares(x, y)
else:
    x = somaImpares(y, x)

print(x)
