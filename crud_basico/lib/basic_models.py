# coding=utf-8
"""Módulo com classes para crud básico de filmes."""

__author__ = 'UnB - Engenharia de Software - GCGVE'

class CategoriaFilme:
    """Classe categoria de filmes (ex: Romance, Terro, Comédia, etc.)."""
    def __init__(self):
        self.__id_categoria = None
        self.__categoria = None

    def get_id_categoria(self):
        return self.__id_categoria

    def get_categoria(self):
        return self.__categoria

    def set_id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria


class Filme:
    """Classe de filmes."""
    def __init__(self):
        self.__id_filme = None
        self.__titulo = None
        self.__categoria = None
        self.__avaliacao = None

    def get_id_filme(self):
        return self.__id_filme

    def get_titulo(self):
        return self.__titulo

    def get_categoria(self):
        """Retorna o objeto da classe CategoriaFilme"""
        return self.__categoria

    def get_avaliacao(self):
        return self.__avaliacao

    def set_id_filme(self, id_filme):
        self.__id_filme = id_filme

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_categoria(self, categoria):
        """Recebe um objeto da classe CategoriaFilme"""
        if isinstance(categoria, CategoriaFilme):
            self.__categoria = categoria
        else:
            self.__categoria = None

    def set_avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    def __str__(self):
        return str({"id_filme": self.__id_filme, "titulo": self.__titulo, \
        "avaliacao": self.__avaliacao, \
        "categoria": {"id_categoria": self.__categoria.get_id_categoria(), "categoria": self.__categoria.get_categoria()}})

    def get_ditc(self):
        return dict({"id_filme": self.__id_filme, "titulo": self.__titulo, \
        "avaliacao": self.__avaliacao, \
        "categoria": {"id_categoria": self.__categoria.get_id_categoria(), "categoria": self.__categoria.get_categoria()}})