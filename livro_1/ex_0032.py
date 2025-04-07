'''
  Exercício 32 - Crie um programa que exibe em
  tela a tabualda de um determinado número fornecido
  pelo usuário.
'''
numero = int(input("Entre com um valor para gerar a tabuada de (1 a 10) * valor: "))

print(f'Gerando tabuada de {numero}\n')
for indice in range(1, numero+1):
    print(f'{indice} * {numero} = {indice*numero}')