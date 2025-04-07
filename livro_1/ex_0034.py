"""
  Exercício 34 - Crie um programa que realize a
  contagem de 1 até 100, usando apenas números ímpares,
  ao final do processo mostre quanto números foram encontrados
  e a soma deles.

  Nota. Acredito haver um error na resolução do exercício
  constante no livro, pois esta se verificando se um número é
  ímpar utiliando N % 3 == 0, porém isso só
  valida se um número é divisível por 3.

  O correto seria utilizar N % 2 != 0, ou seja se o resto da
  divisão de N/2 não for zero, esse número é impar.
"""

quantidade_impares = 0
soma_impares = 0

for n in range(1, 101):
    if n % 2 != 0:
        soma_impares += n
        quantidade_impares +=1

print(f'Total de impares: {quantidade_impares} com soma total de {soma_impares}')