import json
from models.jogo import Jogo

CAMINHO = "data/jogos.json"


def salvar_jogos(listar_jogos):
    dados = []

    for jogos in listar_jogos:
        dados.append(jogos.para_dict())
    with open(CAMINHO, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregar():
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # TODO: transformar em objetos

            lista_jogos = []
            for item in dados:

                jogo = Jogo(item['nome'], item['genero'], item['ano'])
                lista_jogos.append(jogo)
            return lista_jogos

    except:
        return []
