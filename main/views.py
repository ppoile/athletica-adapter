from django.http import HttpResponse
from django.template import RequestContext, loader
from main.models import Stadion

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def sindex(request):
    stadions_list = Stadion.objects.all()
    template = loader.get_template("main/stadion_index.html")
    context = RequestContext(request, dict(stadions_list=stadions_list))
    return HttpResponse(template.render(context))

def sdetail(request, stadion_id):
    stadion = Stadion.objects.get(pk=stadion_id)
    template = loader.get_template("main/stadion_details.html")
    context = RequestContext(request, dict(stadion=stadion))
    return HttpResponse(template.render(context))
