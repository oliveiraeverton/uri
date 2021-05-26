#1176
#função para calcular fibonacci

def fib(t):
    x = 0
    y = 1
    a = t - 1
    
    while a>0:
        fib = x + y
        x = y
        y = fib
        a = a - 1
    print('Fib({}) = {}'.format(t,y))


testes = int(input())

while testes > 0:
    var = int(input())
    
    if var == 0:
        print('Fib(0) = 0')        
        testes = testes - 1
    else:
        fib(var)
        testes = testes - 1
