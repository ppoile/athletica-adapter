from django.http import HttpResponse
from main.models import Stadion

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def sindex(request):
    stadions = Stadion.objects.all()
    output = ", ".join([item.name for item in stadions])
    return HttpResponse(output)

def sdetail(request, stadion_id):
    return HttpResponse("Hello, world. You're looking at detail for stadion %s." % stadion_id)
