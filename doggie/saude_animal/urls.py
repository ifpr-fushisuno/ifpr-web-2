from django.urls import path
from .views import *

urlpatterns = [
  #Criando as rotas de cada pagina vista pelo usuario
  path('dono', DonoView.as_view()),
  path('dono/<int:pk>/', DonoReadUpdateDeleteView.as_view(), name='dono-detail'),
  path('veterinaria', VeterinariaView.as_view()),
  path('veterinaria/<int:pk>/', VeterinariaReadUpdateDeleteView.as_view(), name='veterinaria-detail')
]
