from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola1(request):
    a = '<img src= "https://i.ibb.co/DWHXPdJ/hola.png">'
    return HttpResponse('<h1>Hola Buenas</h1>' + a + '<br>' + '<h2>La siguiente pagina se llama "quieres" </h2>' + '<br>' + '<p>Lorem y algo mas, creo que esta en latin </p>')

def quieres1(request):
    a = '<img src= "https://i.ibb.co/C919m9G/listos.jpg">'
    return HttpResponse('<h1> Quieres? </h1>' + a + '<br>' + '<h2>La pagina de la segunda aplicacion se llama: </h2>' + '<br>' + '<p>"hola2"</p>')