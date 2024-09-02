#Importando os metodos necessarios da biblioteca rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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
  
  def get(self, request):
    donos = Dono.objects.all()
    serializer = DonoSerializer(donos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class DonoReadUpdateDeleteView(APIView):
  def get(self, request, pk):
    dono = get_object_or_404(Dono, pk=pk)
    try:
      dono = Dono.objects.get(pk=pk)
    except Dono.DoesNotExist:
      return Response({'detail': 'Dono não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DonoSerializer(dono)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    dono = get_object_or_404(Dono, pk=pk)
    serializer = DonoSerializer(dono, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
        dono = get_object_or_404(Dono, pk=pk)
        dono.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


  
class VeterinariaView(APIView):
  def post(self, request):
    serializer = VeterinariaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def get(self, request):
    veterinarias = Veterinaria.objects.all()
    serializer = VeterinariaSerializer(veterinarias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class VeterinariaReadUpdateDeleteView(APIView):
  def get(self, request, pk):
    veterinaria = get_object_or_404(Veterinaria, pk=pk)
    try:
      veterinaria = Veterinaria.objects.get(pk=pk)
    except Veterinaria.DoesNotExist:
      return Response({'detail': 'Veterinaria não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VeterinariaSerializer(veterinaria)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    veterinaria = get_object_or_404(Veterinaria, pk=pk)
    serializer = VeterinariaSerializer(veterinaria, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
        veterinaria = get_object_or_404(Veterinaria, pk=pk)
        veterinaria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
