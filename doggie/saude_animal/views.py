#Importando os metodos necessarios da biblioteca rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny 
from rest_framework.authtoken.models import Token

#Importando models e serializers necessarios
from .models import *
from .serializers import *

from django.shortcuts import render

class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny] # Permite acesso público a este endpoint
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Cria o token para o novo usuário
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views para Usuario
class UsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            usuario = Usuario.objects.get(pk=pk)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            serializer = UsuarioSerializer(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Endereço
class EnderecoView(APIView):
    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk = None):
        if pk is None:
            enderecos = Endereco.objects.all()
            serializer = EnderecoSerializer(enderecos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
              endereco = Endereco.objects.get(pk=pk)
              serializer = EnderecoSerializer(endereco)
              return Response(serializer.data, status=status.HTTP_200_OK)
            except Endereco.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        try:
            endereco = Endereco.objects.get(pk=pk)
            serializer = EnderecoSerializer(endereco, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Endereco.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            endereco = Endereco.objects.get(pk=pk)
            endereco.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Endereco.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Dono
class DonoView(APIView):
    def post(self, request):
        # Primeiro, cria o dados do usuário
        usuario_data = request.data.get('usuario')
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        # Cria o dados do veterinário sem o ID do usuário
        dono_data = request.data.get('dono', {})
        
        # Tente validar o serializer do veterinário antes de salvar o usuário
        dono_serializer = DonoSerializerValidate(data=dono_data)
        
        if dono_serializer.is_valid():
            if usuario_serializer.is_valid():
                usuario = usuario_serializer.save()
                dono_data['usuario'] = usuario.id
                
                dono_serializer = DonoSerializer(data=dono_data)
                if dono_serializer.is_valid():
                    dono = dono_serializer.save()
                    return Response({
                        'usuario': usuario_serializer.data, 
                        'dono': dono_serializer.data
                    }, status=status.HTTP_201_CREATED)
                    
                return Response(dono_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(dono_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk=None):
        if pk is None:
            donos = Dono.objects.all()
            serializer = DonoSerializer(donos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            dono = Dono.objects.get(pk=pk)
            serializer = DonoSerializer(dono)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dono.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            dono = Dono.objects.get(pk=pk)
            serializer = DonoSerializer(dono, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dono.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            dono = Dono.objects.get(pk=pk)
            dono.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dono.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Animal
class AnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            animais = Animal.objects.all()
            serializer = AnimalSerializer(animais, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            animal = Animal.objects.get(pk=pk)
            serializer = AnimalSerializer(animal)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
            serializer = AnimalSerializer(animal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Especialidade
class EspecialidadeView(APIView):
    def post(self, request):
        serializer = EspecialidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            especialidades = Especialidade.objects.all()
            serializer = EspecialidadeSerializer(especialidades, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            especialidade = Especialidade.objects.get(pk=pk)
            serializer = EspecialidadeSerializer(especialidade)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Especialidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            especialidade = Especialidade.objects.get(pk=pk)
            serializer = EspecialidadeSerializer(especialidade, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Especialidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            especialidade = Especialidade.objects.get(pk=pk)
            especialidade.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Especialidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Veterinaria
class VeterinariaView(APIView):
    def post(self, request):
        serializer = VeterinariaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            veterinarias = Veterinaria.objects.all()
            serializer = VeterinariaSerializer(veterinarias, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            veterinaria = Veterinaria.objects.get(pk=pk)
            serializer = VeterinariaSerializer(veterinaria)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Veterinaria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            veterinaria = Veterinaria.objects.get(pk=pk)
            serializer = VeterinariaSerializer(veterinaria, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Veterinaria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            veterinaria = Veterinaria.objects.get(pk=pk)
            veterinaria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Veterinaria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Veterinario
class VeterinarioView(APIView):
    def post(self, request):
        # Primeiro, cria o dados do usuário
        usuario_data = request.data.get('usuario')
        usuario_serializer = UsuarioSerializer(data=usuario_data)

        # Cria o dados do veterinário sem o ID do usuário
        veterinario_data = request.data.get('veterinario', {})
        
        # Tente validar o serializer do veterinário antes de salvar o usuário
        veterinario_serializer = VeterinarioSerializerValidate(data=veterinario_data)
        
        if veterinario_serializer.is_valid():
            if usuario_serializer.is_valid():
                usuario = usuario_serializer.save()
                veterinario_data['usuario'] = usuario.id
                
                veterinario_serializer = VeterinarioSerializer(data=veterinario_data)
                if veterinario_serializer.is_valid():
                    veterinario = veterinario_serializer.save()
                    return Response({
                        'usuario': usuario_serializer.data, 
                        'veterinario': veterinario_serializer.data
                    }, status=status.HTTP_201_CREATED)

                return Response(veterinario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(veterinario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            veterinarios = Veterinario.objects.all()
            serializer = VeterinarioSerializer(veterinarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            veterinario = Veterinario.objects.get(pk=pk)
            serializer = VeterinarioSerializer(veterinario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Veterinario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            veterinario = Veterinario.objects.get(pk=pk)
            serializer = VeterinarioSerializer(veterinario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Veterinario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            veterinario = Veterinario.objects.get(pk=pk)
            veterinario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Veterinario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Prontuario
class ProntuarioView(APIView):
    def post(self, request):
        serializer = ProntuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            prontuarios = Prontuario.objects.all()
            serializer = ProntuarioSerializer(prontuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            prontuario = Prontuario.objects.get(pk=pk)
            serializer = ProntuarioSerializer(prontuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Prontuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            prontuario = Prontuario.objects.get(pk=pk)
            serializer = ProntuarioSerializer(prontuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Prontuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            prontuario = Prontuario.objects.get(pk=pk)
            prontuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Prontuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para RegistroSaude
class RegistroSaudeView(APIView):
    def post(self, request):
        serializer = RegistroSaudeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            registros = RegistroSaude.objects.all()
            serializer = RegistroSaudeSerializer(registros, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            registro = RegistroSaude.objects.get(pk=pk)
            serializer = RegistroSaudeSerializer(registro)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RegistroSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            registro = RegistroSaude.objects.get(pk=pk)
            serializer = RegistroSaudeSerializer(registro, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except RegistroSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            registro = RegistroSaude.objects.get(pk=pk)
            registro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RegistroSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Vacina
class VacinaView(APIView):
    def post(self, request):
        serializer = VacinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            vacinas = Vacina.objects.all()
            serializer = VacinaSerializer(vacinas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            vacina = Vacina.objects.get(pk=pk)
            serializer = VacinaSerializer(vacina)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vacina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            vacina = Vacina.objects.get(pk=pk)
            serializer = VacinaSerializer(vacina, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vacina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            vacina = Vacina.objects.get(pk=pk)
            vacina.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vacina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Exame
class ExameView(APIView):
    def post(self, request):
        serializer = ExameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            exames = Exame.objects.all()
            serializer = ExameSerializer(exames, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            exame = Exame.objects.get(pk=pk)
            serializer = ExameSerializer(exame)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exame.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            exame = Exame.objects.get(pk=pk)
            serializer = ExameSerializer(exame, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exame.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            exame = Exame.objects.get(pk=pk)
            exame.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exame.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Alergia
class AlergiaView(APIView):
    def post(self, request):
        serializer = AlergiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            alergias = Alergia.objects.all()
            serializer = AlergiaSerializer(alergias, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            alergia = Alergia.objects.get(pk=pk)
            serializer = AlergiaSerializer(alergia)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Alergia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            alergia = Alergia.objects.get(pk=pk)
            serializer = AlergiaSerializer(alergia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Alergia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            alergia = Alergia.objects.get(pk=pk)
            alergia.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Alergia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Cirurgia
class CirurgiaView(APIView):
    def post(self, request):
        serializer = CirurgiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            cirurgias = Cirurgia.objects.all()
            serializer = CirurgiaSerializer(cirurgias, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            cirurgia = Cirurgia.objects.get(pk=pk)
            serializer = CirurgiaSerializer(cirurgia)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cirurgia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            cirurgia = Cirurgia.objects.get(pk=pk)
            serializer = CirurgiaSerializer(cirurgia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Cirurgia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            cirurgia = Cirurgia.objects.get(pk=pk)
            cirurgia.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cirurgia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Documento
class DocumentoView(APIView):
    def post(self, request):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            documentos = Documento.objects.all()
            serializer = DocumentoSerializer(documentos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            documento = Documento.objects.get(pk=pk)
            serializer = DocumentoSerializer(documento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Documento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            documento = Documento.objects.get(pk=pk)
            serializer = DocumentoSerializer(documento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Documento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            documento = Documento.objects.get(pk=pk)
            documento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Documento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para AtestadoSaude
class AtestadoSaudeView(APIView):
    def post(self, request):
        serializer = AtestadoSaudeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            atestados = AtestadoSaude.objects.all()
            serializer = AtestadoSaudeSerializer(atestados, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            atestado = AtestadoSaude.objects.get(pk=pk)
            serializer = AtestadoSaudeSerializer(atestado)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AtestadoSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            atestado = AtestadoSaude.objects.get(pk=pk)
            serializer = AtestadoSaudeSerializer(atestado, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AtestadoSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            atestado = AtestadoSaude.objects.get(pk=pk)
            atestado.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AtestadoSaude.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para CarteiraVacinacao
class CarteiraVacinacaoView(APIView):
    def post(self, request):
        serializer = CarteiraVacinacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            carteiras = CarteiraVacinacao.objects.all()
            serializer = CarteiraVacinacaoSerializer(carteiras, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            carteira = CarteiraVacinacao.objects.get(pk=pk)
            serializer = CarteiraVacinacaoSerializer(carteira)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CarteiraVacinacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            carteira = CarteiraVacinacao.objects.get(pk=pk)
            serializer = CarteiraVacinacaoSerializer(carteira, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CarteiraVacinacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            carteira = CarteiraVacinacao.objects.get(pk=pk)
            carteira.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CarteiraVacinacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para FichaClinica
class FichaClinicaView(APIView):
    def post(self, request):
        serializer = FichaClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            fichas = FichaClinica.objects.all()
            serializer = FichaClinicaSerializer(fichas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            ficha = FichaClinica.objects.get(pk=pk)
            serializer = FichaClinicaSerializer(ficha)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FichaClinica.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            ficha = FichaClinica.objects.get(pk=pk)
            serializer = FichaClinicaSerializer(ficha, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FichaClinica.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            ficha = FichaClinica.objects.get(pk=pk)
            ficha.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FichaClinica.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Receituario
class ReceituarioView(APIView):
    def post(self, request):
        serializer = ReceituarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            receituarios = Receituario.objects.all()
            serializer = ReceituarioSerializer(receituarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            receituario = Receituario.objects.get(pk=pk)
            serializer = ReceituarioSerializer(receituario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Receituario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            receituario = Receituario.objects.get(pk=pk)
            serializer = ReceituarioSerializer(receituario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Receituario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            receituario = Receituario.objects.get(pk=pk)
            receituario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Receituario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para TermoConsentimento
class TermoConsentimentoView(APIView):
    def post(self, request):
        serializer = TermoConsentimentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            termos = TermoConsentimento.objects.all()
            serializer = TermoConsentimentoSerializer(termos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            termo = TermoConsentimento.objects.get(pk=pk)
            serializer = TermoConsentimentoSerializer(termo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TermoConsentimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            termo = TermoConsentimento.objects.get(pk=pk)
            serializer = TermoConsentimentoSerializer(termo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TermoConsentimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            termo = TermoConsentimento.objects.get(pk=pk)
            termo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TermoConsentimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para AtestadoObito
class AtestadoObitoView(APIView):
    def post(self, request):
        serializer = AtestadoObitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            atestados = AtestadoObito.objects.all()
            serializer = AtestadoObitoSerializer(atestados, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            atestado = AtestadoObito.objects.get(pk=pk)
            serializer = AtestadoObitoSerializer(atestado)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AtestadoObito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            atestado = AtestadoObito.objects.get(pk=pk)
            serializer = AtestadoObitoSerializer(atestado, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AtestadoObito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            atestado = AtestadoObito.objects.get(pk=pk)
            atestado.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AtestadoObito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Procedimento
class ProcedimentoView(APIView):
    def post(self, request):
        serializer = ProcedimentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is None:
            procedimentos = Procedimento.objects.all()
            serializer = ProcedimentoSerializer(procedimentos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            procedimento = Procedimento.objects.get(pk=pk)
            serializer = ProcedimentoSerializer(procedimento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Procedimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            procedimento = Procedimento.objects.get(pk=pk)
            serializer = ProcedimentoSerializer(procedimento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Procedimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            procedimento = Procedimento.objects.get(pk=pk)
            procedimento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Procedimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
def homePage(request):
    return render(request, "saude_animal/home.html")
