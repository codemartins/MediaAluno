print('Olá, caro aluno(a)!')
aluno =  input('Qual é o seu nome? ')
nota1 = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a Nota 2: '))
nota3 = float(input('Digite a Nota 3: '))

media = (nota1 + nota2 + nota2) / 3

print('')

if(media >= 7):
    print('Sua nota foi: ', media, 'e você foi Aprovado.')
    print('Parabens!', aluno)

elif(media >= 5) and (media < 7):
    print('Sua nota foi: ', media, 'e você está em Recuperação!')
    print('Boa sorte!', aluno)

else:
    print('Sua nota foi: ', media, 'e você foi Reprovado(a)')
    print('Se esforce mais na próxima!', aluno)