from rest_framework import serializers
from .models import *


class DonoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dono
    fields = "__all__"

class VeterinariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Veterinaria
    fields = "__all__"

class TipoUsuarioSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = "__all__"


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = "__all__"


class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = "__all__"


class RegistroSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroSaude
        fields = "__all__"


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = "__all__"


class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = "__all__"


class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergia
        fields = "__all__"


class CirurgiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cirurgia
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"


class AtestadoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtestadoSaude
        fields = "__all__"


class CarteiraVacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteiraVacinacao
        fields = "__all__"


class FichaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaClinica
        fields = "__all__"


class ReceituarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receituario
        fields = "__all__"


class TermoConsentimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermoConsentimento
        fields = "__all__"


class AtestadoObitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtestadoObito
        fields = "__all__"


class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = "__all__"
