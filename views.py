from django.shortcuts import render, HttpResponse
from django.template.loader import get_template

# Create your views here.

def Home(request): #PrimeraVista
    #Abriendo_La_Plantilla
    doc_externo=get_template('Home.html')
    #Variables
    titulo_Pagina = 'Empleos_Informaticos_RD'
    #Pasando las variables a la plantilla
    documento=doc_externo.render({
        "Titulo":titulo_Pagina,
    })
    return HttpResponse(documento)

def Programacion(request):#PrimeraVista
    #Abriendo_La_Platinlla
    doc_externo=get_template('Programacion.html')
    #Variables
    titulo_Pagina = 'Empleos_Informaticos_RD_Programacion'
    #Pasando las variables a la plantilla
    documento=doc_externo.render({
        "Titulo": titulo_Pagina,
    })

    return HttpResponse(documento)

def DiseñadorTIC(request):# PrimeraVista
    # Abriendo_La_Platinlla
    doc_externo = get_template('Diseñador.html')
    # Variables
    titulo_Pagina = 'Empleos_Informaticos_RD_Diseñador'
    # Pasando las variables a la plantilla
    documento = doc_externo.render({
        "Titulo": titulo_Pagina,
    })

    return HttpResponse(documento)

def  Ciberseguridad(request):#PrimeraVista
    # Abriendo_La_Platinlla
    doc_externo = get_template('Ciberseguridad.html')
    # Variables
    titulo_Pagina = 'Empleos_Informaticos_RD_Ciberseguridad'
    # Pasando las variables a la plantilla
    documento = doc_externo.render({
        "Titulo": titulo_Pagina,
    })

    return HttpResponse(documento)

def Mecatronica(request):#PrimeraVista
    # Abriendo_La_Platinlla
    doc_externo = get_template('Mecatronica.html')
    # Variables
    titulo_Pagina = 'Empleos_Informaticos_RD_Mecatronica'
    # Pasando las variables a la plantilla
    documento = doc_externo.render({
        "Titulo": titulo_Pagina,
    })

    return HttpResponse(documento)

def IA(request):#PrimeraVista
    # Abriendo_La_Platinlla
    doc_externo = get_template('IA.html')
    # Variables
    titulo_Pagina = 'Empleos_Informaticos_RD_IA'
    # Pasando las variables a la plantilla
    documento = doc_externo.render({
        "Titulo": titulo_Pagina,
    })

    return HttpResponse(documento)

def Admin(request):
    return HttpResponse('Administrador')
