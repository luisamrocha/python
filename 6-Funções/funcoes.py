'''
Atividade 1 - Crie um programa em Python que ofereça um menu para o usuário com as seguintes opções: inverter uma palavra, contar o número de letras de uma palavra e verificar se uma palavra é um palíndromo. Utilize uma estrutura de controle de fluxo while para permitir que o usuário escolha as opções e execute a ação correspondente. Certifique-se de que o programa continue executando até que o usuário decida sair
''' ''''

def inverter_string():
    palavra = input("deseja a palavra que desja inverter: ")
    return palavra[::-1]

def contar_letrar():
    palavra = input("deseja a palavra que desja contar as letras: ")
    return len(palavra)

def palindromo():
    palavra = input("deseja a palavra que deseja verificar se é um palíndromo: ")
    if palavra[0] == palavra[-1] and palavra [1]== palavra[-2]:
        return("a palavra é um palíndromo ")
    else:
        return("a palavra nao é um palíndromo")
    
while True:
    menu = int(input("Clique 1 para inverter a palavra, 2 para contar o numero de letras, 3 para verificar se é um palíndromo: "))
    match menu:
        case 1:
            print(inverter_string())
        case 2:
            print(contar_letrar())
        case 3:
            print(palindromo())
  
''' '''
Atividade 2 - Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
'''

lista = []
while True:
    numeros = int(input("Digite os valores que deseja ou digite 0 para sair do programa: "))
    if numeros == 0:
        break
    lista.append(numeros)

def calcular_media(*nms):
    return (sum(lista))/len(lista)

print(calcular_media(lista))

x= (sum(lista))/len(lista)

def verificar_situacao(x):
    if x == 10:
        return "Parabéns, sua média é 10"
    elif x >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print(verificar_situacao(x))

'''
Atividade 3- Considere uma lista de números inteiros numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
Função filter() para obter uma nova lista com números pares da lista numeros
Função reduce()  para obter a soma de todos os números da lista numeros
Qual o resultado obtido após a execução das operações acima?
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = list(map(lambda numero: numero**2, numeros ))
print(quadrado)

numeros_pares = list(filter(lambda numero: numero%2==0, numeros))
print(numeros_pares)

from functools import reduce
soma = reduce(lambda x,y: x+y,numeros)
print(soma)

'''
Atividade 4- Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.
'''
def media(num1,num2,num3):
    soma = num1+num2+num3
    media = soma/3
    return media

print(media(10,20,10))

'''
Atividade 5- Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.
'''
def maior_numero(num1,num2,num3):
    if num1>num2 and num1>num3:
        return (f'{num1} é o maior número')
    elif num2>num1 and num2>num3:
        return (f'{num2} é o maior número')
    else:
        return (f'{num3} é o maior número ')

print(maior_numero(1,2,3))

'''
Atividade 6- Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.
'''
import random as rd

def lancar_dados():
    dado1 = rd.randint(1,7)
    dado2 = rd.randint(1,7)
    soma = dado1+dado2
    return soma

print(lancar_dados())

'''
Atividade 7- Crie uma função chamada calculadora que receba três parâmetros: dois números (a e b) e uma string (operacao) que indica a operação a ser realizada entre os números. A função deve retornar o resultado da operação indicada.
'''
def calculadora(a,b,operacao):
    if operacao == '+':
        return a + b
    elif operacao == "-":
        return a -b 
    elif operacao == "*":
        return a*b
    elif operacao == "/":
        return a/b
    else:
        return None
    
print(calculadora(2,2,'+'))
print(calculadora(2,2,'-'))
print(calculadora(2,2,'*'))
print(calculadora(2,2,'/'))

'''
Atividade 8- Crie uma função chamada par_impar que receba um número inteiro n e retorne a string "Par" se o número for par, ou "Ímpar" se o número for ímpar.Além disso, crie uma função lambda chamada impar_par que realize a mesma verificação de forma simplificada, retornando "par" ou "impar" conforme o número seja par ou ímpar.
'''

def par_impar(n):
    if n %2 == 0:
        return "Par"
    else:
        return "ímpar"

impar_par = lambda n: "par" if n%2==0 else "impar"

print(par_impar(33))
print(impar_par(10))

'''
Atividade 9 - Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
'''
lista = []
while True:
    numeros = int(input("Digite os valores que deseja ou digite 0 para sair do programa: "))
    if numeros == 0:
        break
    lista.append(numeros)
    

def calcular_media(*nms):
    return (sum(lista))/len(lista)

print(calcular_media(lista))

x= (sum(lista))/len(lista)

def verificar_situacao(x):
    if x == 10:
        return "Parabéns, sua média é 10"
    elif x >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print(verificar_situacao(x))
