from django.shortcuts import get_object_or_404, render
from main.models import Stadion

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def sindex(request):
    stadions_list = Stadion.objects.all()
    context = dict(stadions_list=stadions_list)
    return render(request, "main/stadion_index.html", context)

def sdetail(request, stadion_id):
    stadion = get_object_or_404(Stadion, pk=stadion_id)
    context = dict(stadion=stadion)
    return render(request, "main/stadion_details.html", context)
