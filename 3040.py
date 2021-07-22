testes = int(input())
while testes > 0:
    h, d, g = map(int, input().split())
    if 200 <= h <= 300 and d >= 50 and g >= 150:
        print('Sim')
    else:
        print('Nao')
    testes = testes - 1
