"""
  Exercício 33 - Crie um programa que realiza
  a contagem regressiva de X segundos.

  Nota: originalmente o exercício pede um
  valor fixo de 20s, mas adicionei mais alguns
  requisitos:
  - usuário entra com o valor
  - valor não pode ser menor que 5 e maior que 60 segundos
"""
import time

contagem = -1

while contagem < 10 or contagem > 60:
    contagem = int(input("Entre com o valor de contagem regressiva: "))
    if contagem < 10 or contagem > 60:
        print("Valor nao permitido. Valor deve ser entre")
    else:
        for i in range(contagem, -1, -1):
            print(i)
            time.sleep(1)
    print("Booooom!")