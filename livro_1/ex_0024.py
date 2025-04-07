'''
  Exercício 24 - Crie dua variáveis como dois valores
  numéricos inteiros digitados pelo usuário,
  caso o valor do primeiro número for maior
  que o do segundo, exiba em tela uma mensagem
  de acordo, caso contrário, exiba em tela
  uma mensagem dizendo que o primeiro valor
  digitado é menor que o segundo.
'''

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'O primeiro número { "é maior que o segundo." if  numero_1 > numero_2 else "é menor que o segundo."}')