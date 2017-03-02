class CategoriaFilme:
    """Classe categoria de filmes (ex: Romance, Terro, Comédia, etc.)."""
    def __init__(self, id, categoria):
        self.id = id
        self.categoria = categoria


class Filme:
    """Classe categoria de filmes (ex: Romance, Terro, Comédia, etc.)."""
    def __init__(self, id,  titulo, categoria, avaliacao):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.avaliacao = avaliacao
        

