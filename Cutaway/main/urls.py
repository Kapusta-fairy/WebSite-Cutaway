from django.urls import path
from .views import Lending

urlpatterns = [
    path('', Lending.as_view(), name='lending'),
]
