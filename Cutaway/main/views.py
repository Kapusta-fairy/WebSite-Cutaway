from django.views.generic import ListView
from .models import Gallery


class Lending(ListView):
    model = Gallery
    template_name = 'main/lending.html'
