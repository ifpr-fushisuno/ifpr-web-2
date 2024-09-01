#Importando os metodos necessarios da biblioteca rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando models e serializers necessarios
from .models import Dono, Veterinaria
from .serializers import DonoSerializer, VeterinariaSerializer

#Criando a classe da view
class DonoView(APIView):
  #Criando os metodos http
  def post(self, request):
    #Instanciando os serializer
    serializer = DonoSerializer(data=request.data)
    if serializer.is_valid():
      #Se tudo estiver correto salva no banco
      serializer.save()
      #Retornando a resposta ao front-end e passando o status da requisição
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VeterinariaView(APIView):
  #Criando os metodos http
  def post(self, request):
    #Instanciando os serializer
    serializer = VeterinariaSerializer(data=request.data)
    if serializer.is_valid():
      #Se tudo estiver correto salva no banco
      serializer.save()
      #Retornando a resposta ao front-end e passando o status da requisição
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)