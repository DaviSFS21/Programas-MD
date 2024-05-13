# A ideia deste programa é receber um conjunto e um elemento, e verificar se o elemento é pertinente no conjunto.

import os

os.system('cls')

conj = []

while True:
    elemento = input(f'Insira elementos no conjunto{conj}(Digite "/" para parar): ')
    if elemento == '/':
        os.system('cls')
        break
    conj.append(elemento)

x = input("Digite um elemento para verificar se está no conjunto fornecido: ")

if x in conj:
    print("O elemento está no conjunto.")
else:
    print("O elemento não está no conjunto.")

print()
print("|-----------------------------------------------|")
print("|             Feito por Davi Soares             |")
print("|-----------------------------------------------|")
print()
input("Pressione ENTER para finalizar a execução")