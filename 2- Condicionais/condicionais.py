'''
Atividade 1- Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
'''
velocidade = float(input("Qual a velocidade do carro? "))
multa = 20*(velocidade-80)

if velocidade>80:
    print(f'Você foi multado em {multa} reais por excesso de velocidade')
else:
    print('parabéns, você está dirigindo na velocidade correta')

'''
Atividade 2-Escreva um programa que escolha um número aleatório entre 1 e 100 e peça ao usuário que tente adivinhar o número. O programa deve fornecer dicas informando se o número a ser encontrado é maior ou menor do que o número fornecido pelo usuário.
'''
import random 
numeroaleatorio = random.randint(1,101)
tentativa = int(input("Digite sua tentativa: "))

if tentativa < numeroaleatorio:
    print("Tente novamente um número mais alto!")
elif tentativa > numeroaleatorio:
    print("Tente novamente um número mais baixo!")
else:
    print(f"Parabéns, acertou! o número era {numeroaleatorio}!")

'''
Atividade 3- Escreva um programa que solicite ao usuário que insira sua idade. Com base na idade fornecida, verifique se a pessoa é menor de idade, adulta ou idosa e exiba uma mensagem apropriada
'''
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade and idade< 60:
    print("Você é um adulto.")
else:
    print("Você é idoso.")

'''
Atividade 4- Escreva um programa que solicite ao usuário que insira um nome de usuário e senha.
Verifique se o nome de usuário é "admin" e a senha é "1234". Se ambos forem verdadeiros, exiba uma mensagem de login bem- sucedido; caso contrário, exiba uma mensagem de login inválido.
'''
nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if nome_usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Login inválido!")

"""
Atividade 5-Escreva um programa que solicite ao usuário que insira uma nota de 0 a 100. Com base na nota fornecida, atribua uma classificação ("A", "B", "C", "D" ou "F") e exiba a classificação correspondente.
"""
nota = int(input("Digite uma nota de 0 a 100: "))

if nota >= 90:
    classificacao = "A"
elif 80 <= nota < 90:
    classificacao = "B"
elif 70 <= nota < 80:
    classificacao = "C"
elif 60 <= nota < 70:
    classificacao = "D"
else:
    classificacao = "F"


print(f"A classificação correspondente à nota {nota} é: {classificacao}")

"""
Atividade 6-Escreva um programa que solicite ao usuário que insira sua altura em metros e seu peso em quilogramas. Com base nesses valores, calcule o Índice de Massa Corporal (IMC) e exiba uma mensagem informando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.
"""
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3 (mórbida)"

print(f"Seu IMC é {imc:.2f}. Você está classificado com: {classificacao}")

'''
Atividade 7- Faça um programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input("Digite uma letra : ")

if letra =="a" or letra=="e" or letra =="i" or letra =="o" or letra =="u":
    print(f' a letra {letra} é uma vogal')
else:
    print(f'a letra {letra} é uma consoante ')

'''
Atividade 8- Verificar se um número é par ou ímpar
'''
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

'''
Atividade 9- Escreva um programa que solicite ao usuário que insira a quantidade de produtos que ele deseja comprar. Com base na quantidade fornecida, aplique diferentes descontos e exiba o valor final a ser pago. Descontos de 10, 20 e 30%
'''
quantidade = int(input("Digite a quantidade de produtos que deseja comprar: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))
valor_total = quantidade * preco_unitario

if quantidade <= 10:
    desconto = 0.10  
elif 11 <= quantidade <= 20:
    desconto = 0.20  
else:
    desconto = 0.30 

valor_final = valor_total * (1 - desconto)

print(f"Valor total sem desconto: R${valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100}%")
print(f"Valor final a ser pago: R${valor_final:.2f}")

'''
Atividade 10- Escreva um programa que solicite ao usuário que insira um dia da semana. Verifique se é um dia útil ou um dia de folga e exiba uma mensagem correspondente.
'''
dia_da_semana = input("Digite um dia da semana: ").strip().lower()
if dia_da_semana in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
    print(f"{dia_da_semana.capitalize()} é um dia útil.")
else:
    print(f"{dia_da_semana.capitalize()} é um dia de folga.")