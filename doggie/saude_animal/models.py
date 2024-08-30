from django.db import models

class Documento(models.Model):
    tipo = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to="arquivo")
    id_prontuario = models.ForeignKey(Prontuario, on_delete=CASCADE)

class Exame(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    resultado = models.CharField(max_length=200)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    id_veterinaria = models.ForeignKey(Veterinaria, on_delete=CASCADE)
    
class Monitoramento(models.Model):
    batimentos = models.IntegerField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

class Notificacao(models.Model):
    tipo = models.CharField(max_length=50)
    mensagem = models.CharField(max_length=200)
    data = models.DateField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 