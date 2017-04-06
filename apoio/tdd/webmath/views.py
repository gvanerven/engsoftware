from django.shortcuts import render
from django.http import HttpResponse
import json
from math import sqrt

# Create your views here.

def index(request):
    return HttpResponse("<html><header><meta><title>WebMath</title></meta></header><body><h1>Webmath: Funções de matemática.</h1></body></html>")

def raiz(request, numero=None):
    response = HttpResponse(content_type="application/json")
    numero_float = float(numero)
    if numero_float<0 :
        response.status_code = 404
        response.content = str(json.dumps({"erro":"numero negativo"}))
    else:
        response.status_code = 200
        response.content = str(json.dumps({"raiz":sqrt(float(numero))}))
    return response
