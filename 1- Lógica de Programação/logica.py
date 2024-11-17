#Para quebrar a maldição.... rsrs
print("Hello world :)")

"""
Atividade 1- Crie um exemplo de cada uma das principais tipagens de variáveis. Crie uma solicitação de dados ao usuário.Imprima a solicitação anterior na tela com uma mensagem personalizada.
"""
idade = int(input("digite sua idade "))
print(f'você tem {idade} anos :)')

altura = float(input("digite sua altura "))
print(f'você tem {altura}cm de altura')

nome = str(input("digite seu nome"))
print(f'Seja bem vinda, {nome} ')

a= int(input("Digite um número "))
b= int(input("Digite um outro número  "))
resultado = a>b

'''
Atividade 2 - Escreva um programa que solicite ao usuário que insira uma temperatura em graus Celsius e, em seguida, converta e exiba  temperatura equivalente em graus Fahrenheit. A fórmula de conversão é: Fahrenheit = Celsius * 9/5 + 32.
'''
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5 )+ 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

'''
Atividade 3- Solicite a largura e a altura de um retângulo e calcule a área.
'''
altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))
area = altura*largura
print(f"A área do retângulo é de {area}")

'''
Atividade 4- Solicite o peso e a altura do usuário e calcule o IMC (Índice de Massa Corporal).
'''
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso*(altura**2)
print(f"Seu IMC é de {IMC}")


'''
Atividade 5- Cálculo de média de três números
'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3
print(f"A média dos três números é: {media}")

'''
Atividade 6- Peça um valor em dólares e converta-o para reais. 
'''
valor_em_dolares = float(input("Digite um valor em dólares: "))
taxa_de_cambio = 5
valor_convertido = valor_em_dolares/taxa_de_cambio
print(f"{valor_em_dolares} dolares equivale a {valor_convertido} reais")


'''
Atividade 7- Solicite o diâmetro de um círculo e calcule a circunferência.
'''
diametro = float(input("Digite o diâmetro do círculo: "))
pi = 3.14
circunferencia = pi * diametro
print(f"A circunferência do círculo é {circunferencia}")

'''
Atividade 8- Solicite o nome de um serviço e seu preço, e exiba uma mensagem informando o nome do serviço e o preço com 15% de desconto.
'''
servico = str(input("Digite o nome do serviço: "))
preco = float(input("Digite o preço do serviço: "))
preco_com_desconto = preco * 0.85
print(f"O preço do serviço {servico} com 15% de desconto é {preco_com_desconto:.2f} reais")

'''
Atividade 9- Solicite o nome, profissão e cidade do usuário e exiba essas informações em uma única linha.
'''
nome = str(input("Digite seu nome: "))
profissao = str(input("Digite sua profissão: "))
cidade = str(input("Digite a cidade onde mora: "))
print(f"Seu nome é {nome}, você é {profissao} e mora em {cidade}")

'''
Atividade 10- Solicite dois números ao usuário e calcule a multiplicação.
'''
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))
multiplicacao = primeiro_numero * segundo_numero
print(f"O resultado da multiplicação é {multiplicacao}")


