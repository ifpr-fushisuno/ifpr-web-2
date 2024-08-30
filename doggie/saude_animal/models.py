from django.db import models

class Dono(models.Model):
  nome = models.CharField(max_length=100),
  email = models.CharField(max_length=100),
  senha = models.CharField(max_length=100),
  telefone = models.CharField(max_length=20),
  endereco = models.CharField(max_length=255)

class Animal(models.Model):
  nome = models.CharField(max_length=100),
  raca = models.CharField(max_length=50),
  idade = models.PositiveIntegerField(),
  informacoes_de_saude = models.TextField(),
  id_usuario = models.ForeignKey(Dono, on_delete=models.CASCADE)

class Prontuario(models.Model):
  doencas_cronicas = models.TextField(),
  vacinas = models.TextField(),
  medicamentos = models.TextField(),
  exames = models.TextField(),
  consultas = models.TextField(),
  id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

class Veterinaria(models.Model):
  nome = models.CharField(100),
  crmv = models.CharField(20),
  especialidade = models.CharField(100),
  telefone = models.CharField(20),
  endereco = models.CharField(255)

class Consulta(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    resultado = models.CharField(max_length=200)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    id_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)

class Documento(models.Model):
    tipo = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to="arquivo")
    id_prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)

class Exame(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    resultado = models.CharField(max_length=200)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    id_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)
    
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