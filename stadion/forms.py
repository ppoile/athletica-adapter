from django.forms import ModelForm
from stadion.models import Anlage

class AnlageForm(ModelForm):
   class Meta:
      model = Anlage
      fields = "__all__"

class StadionForm(ModelForm):
   class Meta:
      model = Stadion
      fields = "__all__"
