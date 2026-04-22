class Jogo:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano

    def exibir(self):
        print(f"{self.nome} - {self.genero} ({self.ano})")

    def para_dict(self):
        return {
            "nome": self.nome,
            "genero": self.genero,
            "ano": self.ano,
        }

    @staticmethod
    def de_dict(dados):
        return Jogo(
            nome=dados["nome"],
            genero=dados["genero"],
            ano=dados["ano"]
        )
