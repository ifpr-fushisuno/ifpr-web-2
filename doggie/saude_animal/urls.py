from django.urls import path
from .views import DonoView, VeterinariaView

urlpatterns = [
  #Criando as rotas de cada pagina vista pelo usuario
  path('dono', DonoView.as_view()),
  path('veterinaria', VeterinariaView.as_view())
]