#Algoritmo e Logica
# 1º Passo: Peça para o usuário digitar a primeira nota;
# 2º Passo: Peça para  usuário digitar a a segunda nota;
# 3º Passo: Calcule a media das duas notas
#           (PrimeiraNota + SegundaNota) / 2;
# 4º Passo: Calcule o valor final.
# 5º Se a média for maior que 6, mostre na tela, Aluno Aprovado;
# 6º Se a nota for menor que 6, mostre que o aluno está reprovado.

aluno = input('Qual o nome do Aluno(a)? ')
Pnota = float(input('Qual a primeira nota da Avaliação? ' ))
Snota = float(input('Qual a segunda nota da avaliação? '))

media = (Pnota + Snota) / 2
print('')
print('Olá, ', aluno,'sua nota na AV1 foi: ', Pnota, 'e na AV2: ', Snota)
print('a média da sua nota final foi: ', media, 'pontos.')
print('')

if media < 6 :
    print(aluno, '[RESULTADO] Infelizmente você não atingiu a nota média. :/')
if media >= 6 :
    print('[Resultado] Uhuuuuuuu!,', aluno, 'você foi APROVADO!')