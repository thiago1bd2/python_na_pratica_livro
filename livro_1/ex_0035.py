"""
  Exercício 35 - Crie um programa que
  pede ao usuário que o mesmo digite
  um número qualquer, em seguida se esse
  número é primo, caso não, retorn quantas
  vezes esse número é divisível.
"""

numero = 1
divisoes = 0

while numero <= 1:
    numero = int(input("Entre com um número maior que 1: "))
    if numero > 1:        
        for i in range(1, numero + 1):
              if numero % i == 0:
                   print(f'{numero} % {i} == {numero % i}')
                   divisoes +=1
        print(f'O {numero} {"é primo" if divisoes == 2 else "é divisivel "+str(divisoes)+" vezes"}')
    else:
        print(f'O {numero} não é um valor aceito.')