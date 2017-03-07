from django.test import TestCase
import requests
import json
from crud_basico.lib.basic_models import Filme, CategoriaFilme

# Create your tests here.
class TestAPI(TestCase):
    def setUp(self):
        self.__url = "http://localhost:8000/crudbasico/api/filmes"
        categoria = CategoriaFilme()
        categoria.set_id_categoria(1)
        categoria.set_categoria("Comédia")
        self.__filme_teste = Filme()
        self.__filme_teste.set_id_filme(-1)
        self.__filme_teste.set_titulo("Teste Filme")
        self.__filme_teste.set_categoria(categoria)
        self.__filme_teste.set_avaliacao(4.5)

    def test_insere_filme(self):
        rqst = requests.post(self.__url, json = json.dumps(self.__filme_teste.get_ditc()))
        self.assertEqual(rqst, 201, "Teste de retorno de CREATE")