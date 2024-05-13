# Após receber vários elementos de um conjunto, o programa retorna a cardinalidade do mesmo.

import os

os.system('cls')

conj = []

while True:
    elemento = input(f'Insira elementos no conjunto{conj}(Digite "/" para parar): ')
    if elemento == '/':
        os.system('cls')
        break
    conj.append(elemento)

print(f'A = {sorted(set(conj))}')
print(f'#A = {len(set(conj))}')

print()
print("|-----------------------------------------------|")
print("|             Feito por Davi Soares             |")
print("|-----------------------------------------------|")
print()
input("Pressione ENTER para finalizar a execução")