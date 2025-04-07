'''
  Exercício 31 - Crie um programa que
  realiza a progressão aritmética de 20 elementos,
  com o primeiro termo e razão definidos pelo usuário.
'''

termo = int(input("Entre com o primeiro termo da PA: "))
razao = int(input("Ente com a razão da PA:"))
an = int(input("Quantos termos a calcular: "))

# An = A1 + (n - 1) * r
pa = termo + (10 - 1) * razao # -> 10 + (20 - 1 ) * 4 -> 10 + (19) * 4 -> 10 + 76 -> 86
iteracao = 1
for i in range(termo, pa + razao, razao):
    print(f'Termo nº{iteracao}: {i}')
    iteracao +=1

# Modo menos simples
for i in range(10):
    termo_n = termo + i * razao
    print(f'Termo nº{i}: {termo_n}')

iteracao = an
# Usando while
iteracao = 1
while iteracao <= 10:
    termo_n = termo + (iteracao - 1) * razao
    print(f'Termo nº{iteracao}: {termo_n}')
    iteracao +=1
