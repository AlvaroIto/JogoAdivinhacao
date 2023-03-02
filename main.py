'''
- Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
- Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
- Algum inteiro aleatório será selecionado pelo sistema, o usuário deve adivinhar esse inteiro e, ao acertar o programa
  irá informar o número de tentativas
'''

from random import randint

print('==================================\n'
      '       JOGO DA ADIVINHAÇÃO\n'
      '==================================')

#contador de tentativas
cont = 0

#digitar números
print('Informe o intervalo dos números')
n1 = int(input('Digite o menor número: '))
n2 = int(input('Digite o maior número: '))


#verificar números
if n1 > n2:
    menor = n2
    n2 = n1
    n1 = menor
elif n1 == n2:
    print('Números iguais.')
    print('Informe o intervalo dos números')
    n1 = int(input('Digite o menor número: '))
    n2 = int(input('Digite o maior número: '))

#gerar número aleatório
num = randint(n1, n2)
#Analisando chute
while True:
    chute = int(input('Chute um número: '))
    cont += 1
    if chute < num:
        print(f'Errou, o número gerado é mais alto')
    elif chute > num:
        print('Errou, o número gerado é mais baixo')
    else:
        print(f'Acertou!\n'
              f'Número gerado: {num}\n'
              f'Chute: {chute}\n'
              f'Tentativas: {cont}')
        break

