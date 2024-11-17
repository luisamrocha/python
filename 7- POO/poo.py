'''
Atividade 1 - Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.
A classe Elevador também possui os seguintes métodos:

Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo". Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".

Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".

Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".

Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".
'''

class Elevador:
    def __init__(self, total_capacidade,atual_capacidade,total_andar,atual_andar):
        self.total_capacidade= total_capacidade
        self.atual_capacidade= atual_capacidade
        self.total_andar = total_andar
        self.atual_andar = atual_andar
   
    def subir(self):
        if self.atual_andar<self.total_andar:
            self.atual_andar+=1
            print(f' você acaba de subir 1 andar e está no andar {self.atual_andar}')
        else:
            print("você está no andar mais alto e não consegue mais subir")


    def descer(self):
        if self.total_andar>= (self.atual_andar-1):
            self.atual_andar-=1
            print(f' você acaba de descer 1 andar e está no andar {self.atual_andar}')
        else:
            print("você já está no térreo e não consegue mais descer")


    def entrar(self):
        if self.atual_capacidade<self.total_capacidade:
            self.atual_capacidade+=1
            print(f"Entrando mais uma pessoa, n de pessoas atualmente é {self.atual_capacidade}")
        else:
            print("o elevador está cheio")


    def sair(self):
        if self.atual_capacidade<self.total_capacidade and self.atual_capacidade>=1:
            self.atual_capacidade-=1
            print(f"Saindo mais uma pessoa, n de pessoas atualmente é {self.atual_capacidade}")
        else:
            print("não tem ninguém")


elevador_lacerda= Elevador(10,2,10,1)
elevador_lacerda.descer()
elevador_lacerda.subir()
elevador_lacerda.entrar()
elevador_lacerda.sair()
elevador_lacerda.sair()
elevador_lacerda.sair()
elevador_lacerda.sair()
elevador_lacerda.subir()
elevador_lacerda.subir()

'''
Atividade 2 - Crie um código em Python que contenha as seguintes classes:
A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: "titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes" que imprimirá na saída o título e o autor/editora do material.

A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá o gênero do livro.

A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá a edição da revista.

Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" para mostrar os detalhes de cada material.
'''
class Material:
    def __init__(self,titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
   
    def exibir_informacoes(self):
        return f"o titulo do material é {self.titulo} e o autor/editora é {self.autor_ou_editora}"


class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero


    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()} e o genero do livro é {self.genero}"

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora,edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
   
    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()} e a edicao é {self.edicao}"


livro_do_aladdin = Livro("aladdin", "waltdisney","ficção")
print(livro_do_aladdin.exibir_informacoes())
       
revista_veja = Revista("Pandemia","EditoraAbril",2020)
print(revista_veja.exibir_informacoes())

'''
Atividade 3- Classe Bomba de Combustível:

Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i.tipoCombustivel. ii.valorLitro iii.quantidadeCombustivel
Possua no mínimo esses métodos:
i.abastecerPorValor( )
método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
ii.abastecerPorLitro( )
método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
iii. alterarValor( )
altera o valor do litro do combustível.
iv. alterarCombustivel( )
altera o tipo do combustível.
v.  alterarQuantidadeCombustivel( )
altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba
'''
class BombaCombustivel:
    def __init__(self,tipo_combustivel,valor_litro,qntd_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qntd_combustivel = qntd_combustivel
   
    def abastecerPorValor(self):
        valor = float(input("Digite o valor que gostaria de abastecer: "))
        qntadd = valor/self.valor_litro
        self.qntd_combustivel += valor
        return f'com o valor de {valor} foi adicionado {qntadd}litros em seu tanque de combustivel'

    def abastecerPorLitro(self):
        litro = int(input("Digite a quantidade de litros que deseja adicionar em seu tanque de combustível: "))
        dinheiro = self.valor_litro*litro
        self.qntd_combustivel += litro
        return f'foi adicionado {litro} litros de gasolina em seu tanque e o valor gasto foi de R${dinheiro}'


    def alterarValor(self):
        avalor = float(input("Digite o valor do litro do combustível: "))
        if self.valor_litro != avalor:
            self.valor_litro = avalor
            return f'o valor do litro do combustível agora é de R${avalor}'
        else:
            return "o valor do combustível já era esse"
   
    def alterarCombustivel(self):
        combustivel = input("Digite o tipo de combustível: ")
        if self.tipo_combustivel != combustivel:
            self.tipo_combustivel = combustivel
            return f'o tipo de combustivel agora é {combustivel}'
        else:
            return 'o tipo de combustível já era esse'
   
    def alterarQuantidadeCombustivel(self):
        bombarestante = float(input("Digite a qnt restante de combustivel na bomba: "))
        if bombarestante != self.qntd_combustivel:
            bombarestante = self.qntd_combustivel
            return f'agora a quantidade de combustível restante na bomba é de {bombarestante}'
        else:
            return 'a quantidade restante de combustível na bomba já era essa quantidade'

gasolina = BombaCombustivel("gasolina", 5.60, 30)
print(gasolina.abastecerPorLitro())
print(gasolina.abastecerPorValor())
print(gasolina.alterarCombustivel())
print(gasolina.alterarValor())
print(gasolina.abastecerPorLitro())

'''
Atividade 4- Crie uma classe base chamada Animal que tenha um método chamado falar, o qual imprime uma mensagem genérica, como "Este animal faz um som." Em seguida, crie duas subclasses chamadas Cachorro e Gato que herdem de Animal. Dentro de cada uma dessas subclasses, sobrescreva o método falar para que ele imprima uma mensagem específica para cada animal. Por exemplo, na classe Cachorro, o método falar pode imprimir "O cachorro late." e, na classe Gato, pode imprimir "O gato mia."
'''
class Animal:
    def falar(self):
        return "Este animal faz um sono"

class Cachorro(Animal):
    def falar(self):
        return "O cachorro late"

class Gato(Animal):
    def falar(self):
        return "O gato mia."
    
animal = Animal()
print(animal.falar())
cachorro = Cachorro()
print(cachorro.falar())
gato = Gato()
print(gato.falar())

'''
Atividade 5- Crie uma classe base chamada Veiculo que tenha um método chamado movimentar. Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer veículo está em movimento. Em seguida, crie duas subclasses chamadas Carro e Moto que herdem de Veiculo. Dentro de cada uma dessas subclasses, sobrescreva o método movimentar para imprimir mensagens específicas para cada tipo de veículo. Na classe Carro, o método movimentar deve imprimir "Carro está dirigindo.", enquanto na classe Moto, o método deve imprimir "Moto está acelerando."
'''
class Veiculo:
    def movimentar(self):
        return "Veículo está em movimento"
    
class Carro(Veiculo):
    def movimentar(self):
        return "Carro está dirigindo"
    
class Moto(Veiculo):
    def movimentar(self):
        return "Moto está acelerando."

veiculo = Veiculo()
print(veiculo.movimentar())
carro = Carro()
print(carro.movimentar())
moto = Moto()
print(moto.movimentar())

'''
Atividade 6-Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo


    def depositar(self):
        deposito = float(input("Digite quanto deseja adicionar ao seu saldo: "))
        if deposito >0:
            self.__saldo +=deposito
            print(f'seu deposito de R${deposito} foi efetuado com sucesso.')
        else:
            print("valor inválido")
    def sacar(self):
        saque = float(input("Digite quanto deseja sacar: "))
        if saque<=self.__saldo:
            self.__saldo -= saque
            print(f'seu saque de R${saque} foi efetuado com sucesso ')
        else:
            print("Saldo insuficiente ")
    def exibir_saldo(self):
        print(f' seu saldo atual é de {self.__saldo}')
       


conta = ContaBancaria("Luisa",1000)
conta.depositar()
conta.sacar()
conta.exibir_saldo()

'''
Atividade 7- Crie uma classe em Python que represente um automóvel com funcionalidades de acelerar, frear e ligar/desligar. Considere acelerar como aumentar 10km, e frear como diminuir 10km.
'''
class Automoveis:
    def __init__(self,marca,modelo,maxima,velo_atual, cor = "Branca"):
        self.marca = marca
        self.modelo = modelo
        self.velo_max = maxima
        self.ligado = False
        self.velo_atual = velo_atual
        self.cor = cor
    def ligar_desligar(self):
        if self.velo_atual ==0:
            self.ligado = not self.ligado
        
    def acelerar(self):
        if self.ligado:
            if self.velo_atual + 10 <= self.velo_max:
                self.velo_atual += 10
                print(f'o carro acelerou e agora está em {self.velo_atual}km/h')
            else:
                self.velo_atual= self.velo_max
                print("você atingiu a velocidade máxima e não consegue mais acelerar")
        else:
            print("o carro está desligado")
            
    def frear(self):
        if self.ligado:
            if self.velo_atual-10 >= 0:
                self.velo_atual -=10
            else:
                self.velo_atual = 0
                print("o carro já está parado")    
        else:
            print("o carro está desligado")
    
chevette =Automoveis("GM","SL",140,0)

print(chevette.velo_atual)
print("Cor", chevette.cor)

print(chevette.velo_atual)
chevette.ligar_desligar() 
chevette.acelerar()
chevette.acelerar()
chevette.acelerar()

for a in range(20):
    chevette.acelerar()
    print(f'velocidade atual é {chevette.velo_atual}')
    
for a in range(20):
    chevette.frear()
    print (f'a velocidade atual é {chevette.velo_atual}')

'''
Atividade 8- Crie uma classe em Python que represente um livro e utilize métodos getter e setter para atualizar a situação de disponibilidade do livro
'''
class Livro:
    def __init__(self, titulo:str,autor:str, id:int):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.__situacao:bool = False
    
    #getter
    @property
    def atualizar_situacao(self):
        return self.__situacao
    
    #setter
    @atualizar_situacao.setter
    def atualizar_situacao(self,situacao):
        if situacao == True or situacao == False:
            self.__situaca = situacao
        
picapauamarelo = Livro("Sitio do picapau", "Monteiro Lobato", 1)
aladdin = Livro("Aladdin","WaltDisney",2)
habito=Livro("O poder do habito","Charles Duhigg",3)

picapauamarelo.atualizar_situacao = "Abobora"
print(picapauamarelo.atualizar_situacao) #False 

'''
Atividade 9 -  Crie um encapsulamento em uma classe Python com getters e setters para manipular o saldo de uma conta corrente.
'''
# Encapsulamento 
class ContaCorrente:
    def __init__(self, conta: str, correntista: str):
        self.conta = conta
        self.correntista = correntista
        self.__saldo = 0 #não consegue ser acessada fora da classe em que foi declarada 

    #Getter: (decorator)
    @property 
    def saldo(self):
        senha = "12345"
        if senha == "12345":
            return self.__saldo
    # Setter: (decorator)
    @saldo.setter
    def saldo(self,valor):
        self.__saldo +=valor
        return self.__saldo

ccVinicius = ContaCorrente("1234-5", "Vinicius Costa")
print(ccVinicius.saldo())

'''
Atividade 10 - Projete um sistema de biblioteca com uma classe base ItemBiblioteca e subclasses como Livro e Revista. Adicione métodos para verificar disponibilidade, reservar e emprestar itens, sendo específicos para cada tipo de item bibliotecário.
'''

class ItemBiblioteca:
    def __init__(self, livro, autor, ano, editora):
        self.livro = livro
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.disponibilidade= True
    
    def verificar_disponibilidade(self):
        if self.disponibilidade == True:
            print("Tem disponibilidade")
            self.disponibilidade = False
        else:
            print("Não tem disponibilidade")
        
    def reservar(self):
        if self.disponibilidade== True:
            print("O livro foi reservado")
            self.disponibilidade= False
        else:
            print("o livro já foi reservado")
    
    def emprestar_itens(self):
        if self.disponibilidade == True:
            print("O livro foi emprestado ")
        else:
            print('não é possível emprestar o livro')

class Livro(ItemBiblioteca):
    def __init__(self, livro, autor, ano, editora,paginas):
        super().__init__(livro, autor, ano, editora)
        self.paginas = paginas

class Revista(ItemBiblioteca):
    def __init__(self, livro, autor, ano, editora,propaganda):
        super().__init__(livro, autor, ano, editora)
        self.propaganda = propaganda

itemdeluisa = ItemBiblioteca('o pequeno principe', "j.k rowlings", 1989, "abril")
livrodeluisa = Livro("seja legal", "joaoemaria", 1939, "abril", 19)
revistadeluisa = Revista("capricho", "zeze", 1923,"abril", True)
    
livrodeluisa.verificar_disponibilidade()
livrodeluisa.reservar()
livrodeluisa.emprestar_itens()

'''
Atividade 11 - Implemente um sistema de cadastro de alunos com uma classe base Aluno e subclasses como AlunoGraduacao e AlunoPosGraduacao. Adicione atributos para notas, frequência, e métodos para calcular médias, sendo específicos para cada tipo de aluno.
'''
listagraduação = []
listaposgraduação = []
class Aluno:
    def __init__(self, tipodealuno, nota, frequencia):
        self.tipodealuno= tipodealuno
        self.nota = nota
        self.frequencia= frequencia

    def calcular_media(self):
        self.tipodealuno = int(input("Digite 1 se vc é aluno da graduação e 2 se vc é aluno da pós graduação: "))
        if self.tipodealuno ==1:
            for i in range(1,3):
                self.nota = float(input("Digite sua primeira nota: "))
                listagraduação.append(self.nota)
            media = (sum(listagraduação))/len(listagraduação)
            print (media)
        if self.tipodealuno ==2:
            for i in range(1,3):
                self.nota = float(input("Digite sua primeira nota: "))
                listaposgraduação.append(self.nota)
            media2 = (sum(listaposgraduação))/len(listaposgraduação)
            print(media2)
    
class Graduação(Aluno):
    def __init__(self, tipodealuno, nota, frequencia, curso):
        super().__init__(tipodealuno, nota, frequencia)
        self.curso = curso

class Pos_Graduação(Aluno):
    def __init__(self, tipodealuno, nota, frequencia,superior):
        super().__init__(tipodealuno, nota, frequencia)
        self.superior = superior

naty = Graduação("Graduação", 8,"sim","ads")
luisa = Pos_Graduação("Posgraduação", 10, "sim", " gestão")

naty.calcular_media()
luisa.calcular_media()

'''
Atividade 12 - Desenvolva um programa de simulação de uma empresa de transporte com uma classe base Veiculo e subclasses como Caminhao e CarroPasseio. Adicione métodos para calcular o consumo de combustível, sendo diferentes para cada tipo de veículo.
'''
class Veiculo:
    def __init__(self,combustivel, tamanho,cor, kmrodados):
        self.combustivel = combustivel
        self.tamanho = tamanho
        self.cor = cor
        self.kmrodados = kmrodados

    def consumo_combustivel(self):
        tipo = int(input("Digite 1 se o veiculo for caminhao, e 2 se o veiculo for carro passeio: "))
        if tipo ==1:
            print("quilometragem/quantidade de combustível consumida. x 2 PQ POR SER UM CAMINHAO PESADO GASTA MAIS")
        if tipo ==2:
            print("quilometragem/quantidade de combustível consumida.")
        
class Caminhao(Veiculo):
    def __init__(self, combustivel, tamanho, cor, kmrodados,peso):
        super().__init__(combustivel, tamanho, cor, kmrodados)
        self.peso = peso

class CarroPasseio(Veiculo):
    def __init__(self, combustivel, tamanho, cor, kmrodados, passeio):
        super().__init__(combustivel, tamanho, cor, kmrodados)
        self.passeio = passeio

naty = Veiculo("gasosa", "grande", "rosa","50km")
luisa = Caminhao("gasosa", "grande","verde","40km","150kg")
paulo = CarroPasseio("gasosa", "pequeno", "azul", "30km", "sim")

luisa.consumo_combustivel()
paulo.consumo_combustivel()


