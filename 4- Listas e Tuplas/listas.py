'''
Atividade 1- Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
'''
contador = 0
lista = []
lista_pares = []
lista_impares= []

while contador <10:
    numero = int(input("Digite um número "))
    lista.append(numero)
    contador +=1

soma_pares = 0
soma_impares= 0

for numero in lista:
    if numero %2==0:
        lista_pares.append(numero)
        soma_pares+= numero
    else:
        lista_impares.append(numero)
        soma_impares +=numero

print(f'os numeros pares são {lista_pares}, a quantidade de números pares é {len(lista_pares)} e a soma dos números é {soma_pares}')

print(f'os numeros pares são {lista_impares}, a quantidade de números pares é {len(lista_impares)} e a soma dos números é {soma_impares}')

print(f'todos os números em uma tupla são {tuple(lista)}')

'''
Atividade 2- Escreva uma função que recebe duas listas e retorna uma nova lista contendo apenas os elementos comuns entre as duas listas.
'''
lista3 = []
def elementoscomum(lista1,lista2):
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3

print(elementoscomum([1,2,3,4,5],[2,4,6]))

'''
Atividade 3- Escreva um programa que recebe uma lista de números e retorna a soma dos elementos em posições ímpares.
'''
contador = 0
lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(1, len(lista), 2): 
    contador += lista[i]

print(f'A soma dos elementos nas posições ímpares é {contador}')

'''
Atividade 4- Escreva um programa que recebe uma lista de strings e retorna uma nova lista contendo as strings invertidas.
'''
lista = ["Python", "Back-End","Listas","Programação","Desenvolvimento"]
listainvertida = []

for i in lista:
    invertida = i[::-1]
    listainvertida.append(invertida)
print(listainvertida)

'''
Atividade 5- Escreva uma função que recebe uma lista de números e retorna o segundo maior número da lista.
'''
def segundo_maior(lista):
    lista.sort()
    return lista[1]

print(segundo_maior([2,5,10]))

'''
Atividade 6- Escreva um programa que recebe uma lista de nomes e retorna uma nova lista contendo apenas os nomes que começam com a letra "L".
'''
lista_nomes = ["Lucas", "Lara", "Miguel", "Luana", "Leonardo", "Paulo"]
nomes_com_l = []
for nome in lista_nomes:
    if nome[0] == "L":
        nomes_com_l.append(nome)
print(nomes_com_l)

'''
Atividade 7-Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante para verificar as frutas que foram armazenadas.
'''
listafrutas = ["maça", "uva", "manga", "pera", "banana", "laranja"]
listatupla = tuple(listafrutas)
print(listatupla)

'''
Atividade 8 - Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números únicos da lista original (sem duplicatas).
'''
def numeros_unicos(lista):
    return list(set(lista))

print(numeros_unicos([1, 2, 2, 3, 4, 4, 5]))

'''
Atividade 9 -Escreva um programa que recebe duas listas e retorna uma nova lista contendo todos os elementos das duas listas, mas sem duplicatas.
'''
def combinar_listas(lista1, lista2):
    return list(set(lista1 + lista2))

print(combinar_listas([1, 2, 3], [3, 4, 5]))

'''
Atividade 10 -Escreva um programa que cria uma lista de tuplas, onde cada tupla contém um número e sua respectiva raiz quadrada. A lista deve conter os números de 1 a 10.
'''
import math

lista_tuplas = [(i, math.sqrt(i)) for i in range(1, 11)]
print(lista_tuplas)

'''
Atividade 11 -Crie dois conjuntos contendo os números de 1 a 5 e de 4 a 8, respectivamente. Verifique se eles são conjuntos disjuntos (ou seja, não têm elementos em comum) e imprima o resultado.
'''
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}
controle = False

for i in conjunto1:
    if i in conjunto2:
        controle = True 

if controle == True:
    print("Tem elementos em comum")