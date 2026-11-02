import base64
import getpass
import base64
from multiprocessing.reduction import send_handle

'''while True:
    resposta = input("Deseja continuar? [S/N] ").strip().lower()
    if resposta in ['n', 'nao', 'não']:
        print("saindo do programa")
        break
    elif resposta in ['s', 'sim']:
        print("Contiuando para próxima tela")
        break
    else:
        print("Resposta inválida")'''

class Senha:
    def __init__(self, local, senha, data):
        self.local = local
        self.senha = senha
        self.data = data

    def exibir(self):
        return f'{self.local}, {self.data}'

minha_senha = Senha(local="google", data="12/12/1234", senha="1234")
print(minha_senha.exibir())
