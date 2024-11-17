'''
Atividade 1 - SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

Implementaremos um sistema de cadastro de senha e inicialização do celular utilizando o loop "for". Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
São permitidas 3 tentativas até que o telefone seja bloqueado.
Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.
'''

senha_cadastrada = "adm123"
tentantiva = 3

for i in range(1,4):    
    senha = input("Digite a senha cadastrada: ")
    if senha == senha_cadastrada:
        print("Seja bem-vindo")
    elif tentantiva ==3 or tentantiva==2: 
        tentantiva -= 1
        print(f'Erro ao acessar o sistema, você só tem agora {tentantiva} chances restantes até o bloqueio do telefone')
    else:
        print("Bloqueado o celular")

"""
Atividade 2- Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.'''
"""

email = "luisarocha@gmail.com"
senha = "admadm"


while True:
    emailsolicitado = input("Digite o email cadastrado: ")
    senhacadastrada = input("Digite a senha cadastrada: ")
    if emailsolicitado == email and senhacadastrada == senha:
        print("Seja bem vindo, usuário ")
        break
    else:
        print("Email e/ou senha inválido: ")

'''
Atividade 3- Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
'''

contador = 0
numero2= 0

while True:
    numero = int(input("Digite um número: "))
    if numero != 0:
        numero2 +=numero
        contador +=1
        print(f'a quantidade de números digitados foi de {contador}')
        print(f"a soma dos números é de {numero2}")
        print(f'a média dos números é {numero2/contador}')
    else:
        break

'''
Atividade 4- Peça ao usuário para ele digitar um número e , em seguida, digite a tabuada correspondente do mesmo número, imprimindo no terminal. 
'''
numero = int(input("Digite um número que deseja ver a tabuada "))
for i in range (1,11,1):
    print(f'{numero} x {i} = {numero*i }')

'''
Atividade 5- Fatorial de um número
'''

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")

'''
Atividade 5- Simulador de caixa eletrônico: Crie um programa que simule um caixa eletrônico, permitindo ao usuário realizar operações como saque, depósito e consulta de saldo. Use um laço "while" para continuar executando o programa até que o usuário escolha sair. Utilize a palavra-chave "break" para sair do laço quando o usuário escolher sair.
'''
import random as rd

frutas = ("maçã", "banana", "abacaxi","mamao", "abacate", "siriguela")
fruta = rd.choice(frutas).upper().strip()

for vez in range(3):
    palpite = input("Digite uma fruta: ").upper().strip()
    if palpite == fruta:
        print(f'acertou a fruta era {fruta}')
        break
    else:
        print(f'vc errou, a fruta tem a letra {fruta[rd.randint(0,len(fruta)-1)]}')

'''
Atividade 6- Contador regressivo personalizado: Peça ao usuário para digitar um número e faça um contador regressivo até zero, imprimindo cada número.
'''
numero = int(input("Digite um número para iniciar o contador regressivo: "))
if numero < 0:
    print("Por favor, digite um número positivo.")
else:
    for i in range(numero, -1, -1):
        print(i)

'''
Atividade 7- Imprima os números ímpares de 1 a 100 usando um loop while.
'''
valor = 1
while valor <= 100:
    if valor % 2 != 0:
        print(valor)
    valor += 1

'''
Atividade 8- Calcule a soma dos números de 1 a 50 usando um loop while.
'''
contador = 0 

for i in range(1,51,1):
    contador +=contador

print(f'a soma dos números de 1 a 50 é {contador}')

'''
Atividade 9- Contagem regressiva: Faça um programa que conte de 10 até 1 em ordem decrescente e, em seguida, imprima "FELIZ ANO NOVO!". Use um laço "while" com a palavra-chave "continue" para pular a impressão do número 5.
'''
for i in range(10,0,-1): 
    if i == 5:
        continue
    else:
        print(i)
print("Feliz ano novo")

'''
Atividade 10- Escreva um programa que imprima os caracteres de uma string.
'''
string = "HELLOWORLD"

for letra in string:
    print(letra)
