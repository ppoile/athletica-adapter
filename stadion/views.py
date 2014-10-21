from django.shortcuts import get_object_or_404, render
from stadion.models import Stadion

def index(request):
    stadien = Stadion.objects.all()
    context = dict(stadien=stadien)
    return render(request, "stadion/index.html", context)

def detail(request, stadion_id):
    stadion = get_object_or_404(Stadion, pk=stadion_id)
    anlagen = [item.bezeichnung for item in stadion.anlagen.all()]
    context = dict(stadion=stadion, anlagen=anlagen)
    return render(request, "stadion/details.html", context)

