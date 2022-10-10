from django.http import JsonResponse
from django.views import View
from api.models import vehiculo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class vehiculoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id > 0):
            vehiculos= list(vehiculo.objects.filter(id=id).values())
            if len(vehiculos) > 0:
                Vehiculo = vehiculos[0]
                datos={'message':"Success", 'Vehiculo': Vehiculo}
            else:
                datos={'message':"Vehiculo not found.."}
            return JsonResponse(datos)
        else:
            vehiculos= list(vehiculo.objects.values())
            if len(vehiculos) > 0 :
                datos={'message':"Success", 'vehiculos': vehiculos}
            else: 
              datos={'message':"Vehiculo not found.."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        vehiculo.objects.create(model=jd['model'], year=jd['year'], price=jd['price'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        vehiculos= list(vehiculo.objects.filter(id=id).values())
        if len(vehiculos) > 0:
            vehiculos=vehiculo.objects.get(id=id)
            vehiculos.model=jd['model']
            vehiculos.year=jd['year']
            vehiculos.price=jd['price']
            vehiculos.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Vehiculo not found.."}
        return JsonResponse(datos)


    def delete(self, request, id):
        vehiculos= list(vehiculo.objects.filter(id=id).values())
        if len(vehiculos) > 0:
            vehiculo.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Vehiculo not found.."}
        return JsonResponse(datos)

        

