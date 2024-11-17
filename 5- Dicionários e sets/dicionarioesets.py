'''
Atividade 1- Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
'''

meu_dicionario = dict()
while True:
    variavel = int(input("Digite 1 para para adicionar um aluno, 2 para remover um aluno, 3 para visualizar todos os alunos, 4 para sair do programa "))
    if variavel == 1:
        chave = input("Digite o nome do aluno: ")
        valor = int(input("Digite número de matrícula: "))
        meu_dicionario[chave] = valor
        print(f' o aluno(a) {chave} foi adicionado com o número de matrícula {valor}')
    elif variavel ==2 :
        aluno = input("Digite o nome do aluno que deseja remover: ")
        if aluno in meu_dicionario:
            del meu_dicionario[aluno]
            print(f'o aluno(a) {aluno} foi removido do dicionário')
        else:
            print("O aluno não está dentro do dicionário ")
    elif variavel ==3:
        for nome, matricula in meu_dicionario.items():
            print(f'{nome}:{matricula}')
    elif variavel ==4:
        print("Você saiu do programa")
        break
    else:
        print("Opção inválida")

'''
Atividade 2- Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.
'''
dicionario = dict()

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
email = input("Digite seu email: ")

dicionario["nome"] = nome
dicionario ["telefone"] = telefone
dicionario ["email"] = email

print(f' as informações de contato são {dicionario}')

'''
Atividade 3- Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.
'''
dicionario = dict()
nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço do produto1: "))
nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço do produto2: "))
nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço do produto3: "))
nome4 = input("Digite o nome do produto 4: ")
preco4 = float(input("Digite o preço do produto4: "))
nome5 = input("Digite o nome do produto 5: ")
preco5 = float(input("Digite o preço do produto5: "))

dicionario[nome1] = preco1
dicionario[nome2] = preco2
dicionario[nome3] = preco3
dicionario[nome4] = preco4
dicionario[nome5] = preco5

soma = sum(dicionario.values())
print(f'O preço total da compra foi de R${soma:.2f}')

'''
Atividade 4- Crie uma lista contendo alguns números repetidos. Converta essa lista em um conjunto para remover as duplicatas e, em seguida, converta novamente em uma lista.
'''
lista = [1,2,3,4,5,5,6,6,7,8,9,9,10]
lista2 =[]
sete = set()

for elemento in lista:
    sete.add(elemento)
for element in sete:
    lista2.append(element)
print(lista2)

'''
Atividade 5- Crie um conjunto contendo os números de 1 a 10. Peça ao usuário para digitar um número e remova-o do conjunto, caso ele esteja presente.
'''
conjunto1 = {1,2,3,4,5,6,7,8,9,10}

numero = int(input("Digite um número: "))

if numero in conjunto1:
    conjunto1.remove(numero)
    print(conjunto1)
else:
    print(conjunto1)

'''
Atividade 6-Crie dois conjuntos com alguns elementos cada um. Verifique se um elemento específico pertence a cada conjunto usando o operador in.
'''
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

print(3 in conjunto1)

if 4 in conjunto2:
    print("Tem 4 no set")
    
'''
Atividade 7- Crie um conjunto contendo os números de 1 a 10 e outro conjunto contendo os números de 5 a 15. Realize a união entre os dois conjuntos e imprima o resultado.
'''
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = {5,6,7,8,9,10,11,12,13,14,15}

uniao = conjunto1 | conjunto2
print(uniao)

'''
Atividade 8- Crie um conjunto contendo os números de 1 a 10 e outro conjunto contendo os números de 8 a 15. Realize a interseção entre os dois conjuntos e imprima o resultado.
'''
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = {8,9,10,11,12,13,14,15}

intersecao = conjunto1&conjunto2
print(intersecao)

'''
Atividade 9- Crie um conjunto contendo os números de 1 a 10 e outro conjunto contendo os números de 5 a 15. Realize a diferença entre os dois conjuntos e imprima o resultado.
'''
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = {5,6,7,8,9,10,11,12,13,14,15}

diferenca = conjunto1 - conjunto2
print(diferenca)

'''
Atividade 10- Crie um conjunto contendo os nomes de alguns países. Peça ao usuário para digitar o nome de um país e verifique se ele está presente no conjunto.
'''

paises = {"Brasil", "Argentina", "Mexico", "Australia"}
pais = input("Digite o nome de um país: ")

if pais in paises:
    print("Está presente no conjunto ")
else:
    print("Não ta presente :c ")

'''
Atividade 11-  Crie um dicionário vazio e peça ao usuário para inserir pares de chave-valor até que ele decida parar. Em seguida, exiba o dicionário completo.
'''
dicionario = {}

while True:
    chave= int(input("Digite um chave para dicionário "))
    valor = int(input("Digite um valor "))
    dicionario[chave]= valor
    parar = int(input("1 para sair , 2 para continuar"))
    if parar ==1:
        print(dicionario)
        break

'''
Atividade 12 - Crie um programa que encontre a chave com o maior valor em um dicionário e imprima tanto a chave quanto o valor correspondente.
dicionario = {"Luísa": 21, "Angela": 22, "Nathalia":23, "Jojo": 24 }
'''
lista = []
dicionario1= {}

for  valor in dicionario.values():
    lista.append(valor)

maior = max(lista)

for i in dicionario.keys():
    if dicionario[i] == maior:
        dicionario1[i] = maior
print(dicionario1)

'''
Atividade 13 - Escreva uma codigo que receba um dicionário e um valor inteiro. A codigo deve retornar uma lista contendo todas as chaves do dicionário que possuem o valor fornecido.
'''
dicionario = {"Luísa": 21, "Angela": 22, "Nathalia":23, "Jojo": 24 }
valor = 21
lista = []

for i in dicionario.keys():
    if dicionario[i] == valor:
        lista.append(i)
print(lista)

