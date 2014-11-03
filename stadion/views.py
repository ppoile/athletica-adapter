from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stadion.models import Anlage
from stadion.models import Stadion

class Index(generic.ListView):
    model = Stadion
    context_object_name = "stadien"
    template_name = "stadion/index.html"

class Create(generic.edit.CreateView):
    model = Stadion
    fields = ["name", "bahnen", "bahnengerade", "ueber1000m", "halle"]

class Detail(generic.DetailView):
    model = Stadion
    template_name = "stadion/detail.html"

class Delete(generic.edit.DeleteView):
    model = Stadion
    template_name = "stadion/confirm_delete.html"
    success_url = reverse_lazy("stadion:index")

class Update(generic.edit.UpdateView):
    model = Stadion
    fields = "__all__"

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
