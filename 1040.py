nota1, nota2, nota3, nota4 = map(float, input().split())

media = (nota1*2 + nota2*3 + nota3*4 + nota4)/10

print("Media: {:.1f}".format(media))


if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    media = (exame + media)/2
    if media >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(media))
    else:
        print("aluno reprovado.")
        print("Media final: {:.1f}".format(media))
