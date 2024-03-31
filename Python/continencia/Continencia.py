# A ideia deste programa é analisar dois conjuntos, A e B, e verificar se um é contido no outro ou não.

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


print("Conjunto A: ",conjA)
print("Conjunto B: ",conjB)

AcB = all(item in conjB for item in conjA)
BcA = all(item in conjA for item in conjB)

if AcB & BcA:
    print("A e B possuem todos os elementos iguais")
elif AcB:
    print("A está contido em B")
elif BcA:
    print("B está contido em A")
else:
    print("A não está contido em B, e vice-versa")

print()
print("|-----------------------------------------------|")
print("|             Feito por Davi Soares             |")
print("|-----------------------------------------------|")
print()
input("Pressione ENTER para finalizar a execução")
