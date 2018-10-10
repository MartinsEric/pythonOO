class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas




filme = Filme('Vingadores', 2018, 160)
filme.dar_like()

serie = Serie('Friends', 1994, 10)
serie.dar_like()
serie.dar_like()
serie.dar_like()


print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duração: {filme.duracao} - Likes: {filme.likes}')
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} - Likes: {serie.likes}')
