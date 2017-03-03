# coding=utf-8
"""DAO para os modelos."""
from django.db import connections
from crud_basico.lib.basic_models import Filme, CategoriaFilme

__author__ = 'UnB - Engenharia de Software - GCGVE'

class FilmeDAO():
    """DAO para a classe Filme."""
    def __init__(self):
        self.__erro = None

    def get_cursor(self):
        """Retorna um cursor para consultas"""
        err = None
        cursor = None
        try:
            cursor = connections['default'].cursor()
        except(Exception, err):
            self.__erro = str(err)

        return cursor

    def close_cursor(self, cursor):
        try:
            cursor.close()
        finally:
            pass

    def buscar_filme(self, id_filme):
        """Busca um filme específico"""
        err = None
        filme = Filme()
        categoria = CategoriaFilme()
        cursor = self.get_cursor()

        query = """
                SELECT id_filme, titulo, fk_categoria_filme, ds_categoria, avaliacao FROM crud_basico.filme AS f
                    INNE JOIN crud_basico.categoria_filme as c ON c.id_categoria = f.fk_categoria_filme
                    WHERE id_filme = {}
                """
        query = query.format(id_filme)

        try:
            row = cursor.execute(query).fetchone()
            if row:
                categoria.set_id_categoria(row.fk_categoria_filme)
                categoria.set_categoria(row.categoria)
                filme.set_id_filme(row.id_filme)
                filme.set_titulo(row.titulo)
                filme.set_categoria(categoria)
                filme.set_avaliacao(row.avaliacao)
            else:
                filme = None
        except(Exception, err):
            print("Falha buscando filme " + filme.get_titulo() + ": " + str(err))
        finally:
            self.close_cursor(cursor)

        return filme

    def insere_filme(self, filme):
        """Insere um Filme"""
        err = None
        id_filme = -1
        if isinstance(filme, Filme):
            cursor = self.get_cursor()
            try:
                id_filme = cursor.execute("SELECT nextval('crud_basico.filmes') as id_filme;").fetchone().id_filme

                query = """
                        INSERT INTO crud_basico.filme (id_filme, titulo, fk_categoria_filme, avaliacao) VALUES ({}, '{}', {}, {})
                        """
                query = query.format(id_filme, filme.get_titulo(), \
                                filme.get_getegoria().get_id_categoria(), filme.get_avaliacao())
                num_insert = cursor.execute(query)
                if num_insert < 1:
                    id_filme = -1
                cursor.commit()
            except(Exception, err):
                print("Falha inserindo filme " + filme.get_titulo() + ": " + str(err))
            finally:
                self.close_cursor(cursor)

        return id_filme
