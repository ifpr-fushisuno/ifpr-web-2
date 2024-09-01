from rest_framework import serializers
from .models import Dono, Veterinaria

class DonoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dono
    fields = "__all__"

class VeterinariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Veterinaria
    fields = "__all__"