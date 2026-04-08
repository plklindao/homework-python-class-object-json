class Jogo:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano

    def exibir(self):
        print(f"{self.nome} - {self.genero} ({self.ano})")

    def para_dict(self):
        # TODO: completar
        pass

    @staticmethod
    def de_dict(dados):
        # TODO: completar
        pass
