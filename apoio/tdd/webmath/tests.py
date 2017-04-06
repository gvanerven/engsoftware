from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json
from math import sqrt

# Create your tests here.

class TestWebmathCalculaRaiz(TestCase):
    """
    Descrição
    """
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def connect_create_raiz(self, numero):
        response = self.client.get(reverse(viewname='webmath/raiz',  kwargs={"numero": numero}),
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        return response

    def test_raiz_conn_code_200(self):
        response = self.connect_create_raiz(0)
        self.assertEqual(response.status_code, 200)

    def test_raiz_val_return_raiz(self):
        response = self.connect_create_raiz(0)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue("raiz" in data)
    
    def test_raiz_correta(self):
        response = self.connect_create_raiz(4)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(sqrt(4),float(data["raiz"]))

    # def test_raiz_invalida(self):
    #     response = self.connect_create_raiz(-4)
    #     data = json.loads(response.content.decode('utf-8'))
    #     self.assertTrue("erro" in data)
    #     self.assertEqual(response.status_code, 404)
        
        
