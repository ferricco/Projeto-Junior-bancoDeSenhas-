while True:
    resposta = input("Deseja continuar? [S/N] ").strip().lower()
    if resposta in ['n', 'nao', 'não']:
        print("saindo do programa")
        break
    elif resposta in ['s', 'sim']:
        print("Contiuando para próxima tela")
        break
    else:
        print("Resposta inválida")
