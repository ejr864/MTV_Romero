from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
def inicio(request):
    return HttpResponse("hola desde django hoy domingo 20:38")


def familiar(request):
    familiar1 =  Familiar(nombre = "Juan", edad = 60, anio_nacimiento = "1988-01-01")
    familiar1.save()
    familiar2 =  Familiar(nombre = "Jose", edad = 34, anio_nacimiento = "1999-02-06")
    familiar2.save()
    familiar3 =  Familiar(nombre = "Miguel", edad = 22, anio_nacimiento = "2000-10-01")
    familiar3.save()
    familiar4 =  Familiar(nombre = "Johanna", edad = 27, anio_nacimiento = "2010-09-05")
    familiar4.save()
    familiar5 =  Familiar(nombre = "Laura", edad = 25, anio_nacimiento = "1980-11-06")
    familiar5.save()
    return render(request, "familiares.html", {"familiares": [familiar1, familiar2, familiar3, familiar4, familiar5]})

#def familiar(request):
#    return render(request, "padre.html",{})


#def familiar(request):
#    return HttpResponse("hola desde familiar")
    
#def familiar(request):
#    familiar1 =  familiar("Juan", 60, "1988-01-01")
#    familiar1.save()
#    return render(request, "familiares.html", {"familiar1": familiar1})
