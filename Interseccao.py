# Após receber os conjuntos, o programa verifica elementos em comum entre eles.

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

conjA = set(conjA)
conjB = set(conjB)

intersAB = sorted(list(conjA & conjB))

print("Conjunto A: ",conjA)
print("Conjunto B: ",conjB)

print("\n")
print("Conjunto A ^ B: ",intersAB)

print()
print("|-----------------------------------------------|")
print("|             Feito por Davi Soares             |")
print("|-----------------------------------------------|")
print()
input("Pressione ENTER para finalizar a execução")