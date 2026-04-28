VERMELHO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"

from models.jogo import Jogo
from services.jogo_service import salvar_jogos, carregar
jogo = carregar()

print("=== SISTEMA DE JOGOS ===")

while True:
    print("\n1 - Adicionar jogo")
    print("2 - Listar jogos")   
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        # TODO: criar jogo
        print("Criar jogo")
        nome = input("Nome: ")

        while True:
            genero = input("Gênero: ")
            if genero.replace(" ", "").isalpha() and len(genero) > 0:
                break
            else:
                print(VERMELHO + "Erro: Gênero deve conter apenas letras." + RESET)

        while True:
            try:
                entrada_ano = input("Ano: ")
                ano = int(entrada_ano)
                
                if len(entrada_ano) == 4:
                    break
                else:
                    print(VERMELHO + "Erro: Digite um ano válido com 4 dígitos (ex: 2026)." + RESET)
                
            except ValueError:
                print(VERMELHO + "Erro: Digite apenas números para o ano!" + RESET)


        novo_jogo = Jogo(nome, genero, ano)
        jogo.append(novo_jogo)
        salvar_jogos(jogo)
        print(VERDE + "Jogo cadastrado!" + RESET)

    elif opcao == "2":
        # TODO: listar jogos
        print("\n Lista de jogos")
        if len(jogo) == 0:
            print("Nenhum jogo cadastrado")
        else:
            for i, JG in enumerate(jogo):
                print("Jogo", i)
                JG.exibir()

    elif opcao == "3":
        print("Saindo do Sistema... ")
        break

    else:
        print("Opção inválida")
