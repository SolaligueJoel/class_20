from django.shortcuts import render
from AppVuelos.models import Vuelos
from datetime import datetime



# Create your views here.
def nuevo_vuelo(request):
    fecha_actual = datetime.now()
    vuelo_nuevo = Vuelos(nombre="Joel",apellido="Solaligue",fecha_ida=fecha_actual)
    vuelo_nuevo.save()
    
    return render(request, 'nuevo_vuelo.html')

def mostrar_vuelos(request):
    consulta_db = Vuelos.objects.all() # Consultamos la db
    
    return render(request, 'mostrar_vuelos.html', {'vuelos':consulta_db})