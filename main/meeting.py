from django.views.generic import DetailView
from django.views.generic import ListView
from main.models import Meeting


class MeetingIndex(ListView):
    model = Meeting
    context_object_name = "meetings"
    template_name = "main/meeting-index.html"

class MeetingDetail(DetailView):
    model = Meeting
    template_name = "main/meeting-detail.html"
