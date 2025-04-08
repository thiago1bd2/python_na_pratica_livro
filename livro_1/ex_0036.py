"""
  Exercício 36 - Crie um programa que pede
  ao usuário digitar uma palavra ou frase,
  verifique se esse conteúdo é um palindromo
  ou não, exibindo em tela esse resultado.
"""

# Forma trabalhosa
texto = str(input("Digite uma palavra ou frase: ")).strip().upper()
print(texto)
palavras = texto.split()
texto_invertido = ''
for i in range(len(palavras)-1, -1, -1):
    print(f'{palavras[i]}')
print(texto_invertido)
