class Programa:

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


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
