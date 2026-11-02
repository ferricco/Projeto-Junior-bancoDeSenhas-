from datetime import datetime
import getpass
import base64
import csv

senhas = []

class Senha:
    def __init__(self, senha, local, data):
        self.senha = senha
        self.local = local
        self.data = data

    def exibir(self):
        return f'{self.local}, {self.data}'

    def buscar(self):
        return f'{self.local}, {self.senha}'

def carregar_senhas():
    try:
        with open('senhas.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha or "," not in linha:
                    continue
                senha, local, data = linha.split(",")

                cadastro = Senha(local=local, senha=senha, data=data)
                senhas.append(cadastro)
    except FileNotFoundError:
        print("Esse arquivo não existe!")


def adicionar():
    while True:
        local = input("A senha pertence ao login de qual Site?")  # identificar a origem da senha

        senha = getpass.getpass(prompt="Digite a senha do login: ", stream=None)
        senha_bytes = senha.encode("utf-8")
        bytes_codificada = base64.b64encode(senha_bytes)
        senha_codificada = bytes_codificada.decode("utf-8")

        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y %H:%M:%S")

        cadastro = Senha(senha=senha_codificada, local=local, data=data)
        senhas.append(cadastro)

        salvar_senhas()

        while True:
            nova_senha = input("Deseja cadastrar mais uma senha? sim ou não: ").strip().lower()
            if nova_senha in ("nao", "não", "n"):
                return
            elif nova_senha in ("sim", "s"):
                break
            else:
                print("Digite apenas sim ou não!")

def listar():
    if not senhas:
        print("Ainda não existe senhas cadastradas!")
    else:
        for cadastro in senhas:
            print(cadastro.exibir())
            print("-" * 30)

def buscar():
    while True:
        encontrado = False

        login = input("Digite o login que você quer buscar a senha: ")

        for cadastro in senhas:
            if cadastro.local == login:
                senha = cadastro.senha
                bytes_codificada = senha.encode("utf-8")
                bytes_original = base64.b64decode(bytes_codificada)
                senha_original = bytes_original.decode("utf-8")
                print(f"{login}: {senha_original}")
                encontrado = True

        if not encontrado:
            print("Esse login não existe!")

        while True:
            novamente = input("Quer continuar a busca? sim ou não ").lower().strip()
            if novamente in ("nao", "não", "n"):
                return
            elif novamente in ("sim", "s"):
                break
            else:
                print("Digite uma opção válida! Sim ou Não")


def menu():
    continuar = True

    while continuar:
        try:
            opcao = int(input("Selecione a opção que deseja: \n"
                              "1 - Adicionar senha\n"
                              "2 - Listar todas as senhas\n"
                              "3 - Buscar senha\n"
                              "4 - Sair\n"))

            if opcao == 1:
                adicionar()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                buscar()
            elif opcao == 4:
                continuar = False
            else:
                print("--- Digite uma opção válida entre 1 e 4 ---")

        except ValueError:
            print("--- Escolha uma opção válida ---")


def salvar_senhas():
    with open('senhas.txt', 'w', encoding='utf-8') as arquivo:
        for cadastro in senhas:
            arquivo.write(f"{cadastro.local},{cadastro.senha},{cadastro.data}\n")
        print("Senha salva com sucesso!")


carregar_senhas()
menu()
for item in senhas:
    print(item.local, item.data, item.senha)