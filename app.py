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
        genero = input("Genero: ")
        ano = input("Ano: ")

        novo_jogo = Jogo(nome, genero, ano)
        jogo.append(novo_jogo)
        salvar_jogos(jogo)
        print("Jogo cadastrado!")

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
