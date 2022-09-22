from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

a = random.randint(1,200)
b = random.randint(100,200)
c = random.randint(1,20)
d = random.randint(120,200)

ip = (a,'.',b,'.',c,'.',d)


def hola2(request):
    return HttpResponse('<h1>Me llamo: Hector Daniel Gatica San Martín</h1>' + '<br>' + '<h2>La siguiente pagina se llama "dato" </h2>' + '<br>' + '<p>Lorem y cosas en latin</p>')

def dato(request):
    ms = "<h1>Mi Ip es: </h1>" + str(ip)
    i = '<img src="https://i.redd.it/jf5ql9wfy0381.jpg" width="300" height="300" >'
    return HttpResponse(ms + '<br>' + i + '<br>' + '<h3> Porfa profe, necesito un 7.0 o me voy a: </h3>' + '<h1>Diseño Grafico</h1>')