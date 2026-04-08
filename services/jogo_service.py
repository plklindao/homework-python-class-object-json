import json
from models.jogo import Jogo

CAMINHO = "data/jogos.json"

def salvar(lista):
    # TODO: converter lista para dicionário
    pass


def carregar():
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # TODO: transformar em objetos
            pass

    except:
        return []
