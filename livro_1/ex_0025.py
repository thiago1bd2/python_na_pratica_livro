'''
  Exercício 25 - Peça para que o usuário digite
  um número, em seguida exiba em tela uma mensagem
  dizendo se tal número é PAR ou ÍMPAR.
'''

numero = int(input("Entre com um número:"))
print(f'O {numero} é {"par" if numero % 2 == 0 else "ímpar"}')