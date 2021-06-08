#1047

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if minuto_final < minuto_inicial:
  hora_final -= 1
  minuto_final +=60
if hora_final < hora_inicial:
  hora_final += 24


hora_jogada = hora_final - hora_inicial
minuto_jogado = minuto_final - minuto_inicial



if hora_inicial == hora_final and minuto_inicial == minuto_final:
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
  print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_jogada, minuto_jogado))
