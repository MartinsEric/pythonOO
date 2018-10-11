class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
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

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self._likes} likes'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - {self.temporadas} temporadas - {self._likes} likes'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme('Vingadores', 2018, 160)
vingadores.dar_like()

friends = Serie('Friends', 1994, 10)
friends.dar_like()
friends.dar_like()
friends.dar_like()

the100 = Serie('The 100', 2013, 5)
the100.dar_like()
the100.dar_like()


sherlock = Serie('Sherlock', 2010, 4)


filmes_e_series = [vingadores, friends,the100, sherlock]

playlist_fds = Playlist('Playlist de fim de semana', filmes_e_series)

for programa in playlist_fds.listagem:
    print(programa)
