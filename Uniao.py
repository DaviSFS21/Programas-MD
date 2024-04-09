# O programa recebe dois conjuntos e une seus elementos, formando o conjunto AB.

import os

os.system('cls')

conjA = []
conjB = []

def ins_elementos(conj,nome):
    while True:
        elemento = input(f'Insira elementos no conjunto {nome}{conj}(Digite "/" para parar): ')
        if elemento == '/':
            os.system('cls')
            break
        conj.append(elemento)
        
ins_elementos(conjA,"A")
ins_elementos(conjB,"B")

unirAB = conjA + conjB
conjAB = sorted(list(set(unirAB)))

print("Conjunto A: ",conjA)
print("Conjunto B: ",conjB)

print("\n")
print("Conjunto A v B: ",conjAB)

print()
print("|-----------------------------------------------|")
print("|             Feito por Davi Soares             |")
print("|-----------------------------------------------|")
print()
input("Pressione ENTER para finalizar a execução")