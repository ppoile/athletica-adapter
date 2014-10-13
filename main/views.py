from django.http import Http404
from django.shortcuts import render
from main.models import Stadion

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def sindex(request):
    stadions_list = Stadion.objects.all()
    context = dict(stadions_list=stadions_list)
    return render(request, "main/stadion_index.html", context)

def sdetail(request, stadion_id):
    try:
        stadion = Stadion.objects.get(pk=stadion_id)
    except Stadion.DoesNotExist:
        raise Http404
    context = dict(stadion=stadion)
    return render(request, "main/stadion_details.html", context)
