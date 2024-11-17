'''
GERENCIADOR DE TAREFAS DIÁRIAS
Configuração do Ambiente Virtual:
Crie um ambiente virtual utilizando o módulo venv para isolar as dependências do projeto.
Definição de Dados:
Utilize estruturas de dados, como dicionários, para representar as tarefas. Cada tarefa deve conter informações como nome, descrição, prioridade e categoria.
Funções:
Implemente funções para adicionar tarefas, listar tarefas, marcar tarefas como concluídas, exibir tarefas por prioridade ou categoria, e outras funcionalidades desejadas.
Menu de Comandos:

Desenvolva um menu de comandos de linha de comando que permita ao usuário interagir com o programa. Este menu deve oferecer opções para realizar operações como adicionar, listar, marcar como concluídas e visualizar tarefas por prioridade ou categoria.
O projeto será organizado em partes distintas, utilizando diversas estruturas de dados e funções para oferecer uma experiência completa de gerenciamento de tarefas aos usuários.
'''
lista_tarefas = dict()
contadordetarefas = 0

def adicionar_tarefa():
    global contadordetarefas
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    categoria = int(input("Digite 1 para adiciona-la na categoria Casa, e 2 para adiciona-la na categoria Trabalho: "))
    contadordetarefas +=1
    lista_tarefas[contadordetarefas]= {'Tarefa': tarefa , 'Categoria': categoria, 'Concluída': False}
    return lista_tarefas

def listar_tarefas():
    for chave, valor in lista_tarefas.items():
        print(f' {chave}: {valor}')

def marcar_tarefas():
    inteiro = int(input("Escolha qual o código da tarefa que vc deseja marcar como concluída: "))
    if inteiro in lista_tarefas:
        if lista_tarefas[inteiro]["Concluída"] == True:
            print("A tarefa já havia sido concluída ")
        elif lista_tarefas[inteiro]["Concluída"] == False:
            lista_tarefas[inteiro]['Concluída']= True
            print(f"Você acaba de marcar como concluída a tarefa {lista_tarefas[inteiro]['Tarefa']}")

def exibir_categoria():
    codigo = int(input("Digite 1 para ver as tarefas da categoria Casa, e 2 para ver as tarefas da categoria Trabalho: "))
    print(f'Tarefas da Categoria {"Casa" if codigo == 1 else "Trabalho"}:')
    for chave, valor in lista_tarefas.items():
        if valor["Categoria"] == codigo:
            print(f' {chave}: {valor}')

while True:
    opção = int(input("Clique 1 para adicionar tarefa, 2 para listar as tarefas, 3 para marcar tarefa como concluída, 4 para exibir tarefa por categoria, 5 para sair do programa: "))
    if opção ==1:
        print(adicionar_tarefa())
    elif opção ==2:
        listar_tarefas()
    elif opção ==3:
        marcar_tarefas()
    elif opção ==4:
        exibir_categoria()
    elif opção ==5:
        print("Vc saiu do programa")
        break
    else:
        print("Opção inválida")
