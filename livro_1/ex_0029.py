'''
  Exercício 29 - Crie um programa que lê
  um valor de início e um valor de fim, exibindo em tela
  a contagem dos números dentro desse intervalo.
'''

inicio_range = int(input("Ente com o inicio do range: "))
fim_range = int(input("Entre com o fim do range: "))

for indice in range(inicio_range, fim_range+1):
    print(indice)