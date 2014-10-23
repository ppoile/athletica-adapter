from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.models import Anlage
from stadion.models import Stadion

def index(request):
    stadien = Stadion.objects.all()
    context = dict(stadien=stadien)
    return render(request, "stadion/index.html", context)

def details(request, stadion_id):
    stadion = get_object_or_404(Stadion, pk=stadion_id)
    context = dict(stadion=stadion)
    return render(request, "stadion/details.html", context)

def vote(request, stadion_id):
    stadion = get_object_or_404(Stadion, pk=stadion_id)
    try:
        selected_anlage = stadion.anlagen.get(pk=request.POST['anlage'])
    except (KeyError, Anlage.DoesNotExist):
        # Redisplay the question voting form.
        context = dict(stadion=stadion, error_message="You did not select a choice.")
        return render(request, 'stadion/details.html', context)
    else:
        #selected_anlage.votes += 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('stadion:details', args=(stadion.xstadion,)))
