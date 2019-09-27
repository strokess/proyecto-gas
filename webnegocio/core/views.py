from django.shortcuts import render, HttpResponse
#En este se definen las vistas de una app
#HttpResponse, sirve para ocupar comandos de html

def inicio(request):
    return render(request, "core/inicio.html") #Instrucción que manda a llamar la plantilla 

#def clientes(request):
 #   return render(request, "core/clientes.html")

#def compras(request):
 #   return render(request, "core/compras.html")

#def ventas(request):
 #   return render(request, "core/ventas.html")

#def reportes(request):
 #   return render(request, "core/reportes.html")

