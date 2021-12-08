def calculaData(horaInicial, minutoInicial, segundoInicial, horaFinal, minutoFinal, segundoFinal):
  if segundoFinal < segundoInicial:
    #entao a subtracao nao eh possivel, para contornar o problema pedimos emprestado para os minutos 60 segundos
    minutoFinal -= 1
    segundoFinal += 60
    resultadoSS = segundoFinal - segundoInicial
  else:
    resultadoSS = segundoFinal - segundoInicial
  if minutoFinal < minutoInicial:
    #entao a subtracao nao eh possivel, para contornar o problema pedimos emprestado para as horas 60 minutos
    horaFinal -= 1
    minutoFinal += 60
    resultadoMM = minutoFinal - minutoInicial
  else:
    resultadoMM = minutoFinal - minutoInicial

  resultadoHH = horaFinal - horaInicial
  return "{}:{}:{}".format(resultadoHH, resultadoMM, resultadoSS)
texto, diaInicial = map(str, input().split())
hhi, mmi, ssi = map(int, input().split(" : "))
texto, diaFinal = map(str, input().split())
hhf, mmf, ssf = map(int, input().split(" : "))
if diaInicial == diaFinal:
  #entao o envento começa e termina no mesmo dia
  x = calculaData(hhi, mmi, ssi, hhf, mmf, ssf)
  fatiamentoHora = x[0:x.find(":")]
  fatiamentoMinuto = x[x.find(":")+1 : x.find(":", x.find(":")+1)]
  fatiamentoSegundo = x[x.find(":", x.find(":")+1)+1:]
  
  print("0 dia(s)")
  print("{} hora(s)".format(fatiamentoHora))
  print("{} minuto(s)".format(fatiamentoMinuto))
  print("{} segundo(s)".format(fatiamentoSegundo))
else:
  diasCorridos = int(diaFinal) - int(diaInicial)
  if hhf > hhi:
    #entao ocorreu diasCorridos
    #calculaData + diasCorridos * 24
    x = calculaData(hhi, mmi, ssi, hhf, mmf, ssf)
    fatiamentoHora = x[0:x.find(":")]
    fatiamentoMinuto = x[x.find(":")+1 : x.find(":", x.find(":")+1)]
    fatiamentoSegundo = x[x.find(":", x.find(":")+1)+1:]
    print("{} dia(s)".format(diasCorridos-1))
    print("{} hora(s)".format(fatiamentoHora))
    print("{} minuto(s)".format(fatiamentoMinuto))
    print("{} segundo(s)".format(fatiamentoSegundo))
  else:
    x = calculaData(hhi, mmi, ssi, hhf, mmf, ssf)
    fatiamentoHora = x[0:x.find(":")]
    fatiamentoMinuto = x[x.find(":")+1 : x.find(":", x.find(":")+1)]
    fatiamentoSegundo = x[x.find(":", x.find(":")+1)+1:]
    if(int(fatiamentoHora)+24 == 24):
      fatiamentoHora = 0
      diasCorridos = 1
      print("{} dia(s)".format(diasCorridos))
      print("{} hora(s)".format(int(fatiamentoHora)))
    else:
      print("{} dia(s)".format(diasCorridos-1))
      print("{} hora(s)".format(int(fatiamentoHora)+24))
    print("{} minuto(s)".format(fatiamentoMinuto))
    print("{} segundo(s)".format(fatiamentoSegundo))
