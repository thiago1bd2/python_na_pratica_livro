'''
  Exercício 16 - Solicite ao usuário
  a entrada de dois valores. Em seguida
  mostra a soma, subtracao, multiplicacao, divisao
  e a potencia do primeiro pelo sengundo valor.
'''
num_1 = int(input('Me dê um número: '))
num_2 = int(input('Agora outro número: '))

lista_de_operacoes = ['+','-','*','/','**']
for operacao in lista_de_operacoes:
  match operacao:
    case '+':
      print(f'{num_1} {operacao} {num_2} = {num_1+num_2}')
    case '-':
        print(f'{num_1} {operacao} {num_2} = {num_1-num_2}')
    case '*':
        print(f'{num_1} {operacao} {num_2} = {num_1*num_2}')
    case '/':
        print(f'{num_1} {operacao} {num_2} = {num_1/num_2}')
    case '**':
        print(f'{num_1} {operacao} {num_2} = {num_1**num_2}')
    case _:
        print('Operaco invalida!')