from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone


class TipoUsuario(models.TextChoices):
    ADMINISTRADOR = 'Administrador', 'Administrador'
    VETERINARIO = 'Veterinário', 'Veterinário'
    DONO = 'Dono', 'Dono'



class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{5}-?\d{3}$')])

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}"

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    senha = models.CharField(max_length=128) 
    tipo = models.CharField(max_length=20, choices=TipoUsuario.choices)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultimo_acesso = models.DateTimeField(auto_now=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def autenticar(self, senha_fornecida: str) -> bool:
        return self.senha == senha_fornecida  

    def tem_permissao(self, permissao: str) -> bool:
        # Lógica para verificar permissões podem ser implementadas aqui.
        pass

    def __str__(self):
        return self.nome


class Dono(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tutor = models.ForeignKey(Dono, on_delete=models.CASCADE)

    def validar_data_nascimento(self):
        return self.data_nascimento <= timezone.now().date()

    def __str__(self):
        return self.nome


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Veterinaria(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Veterinario(models.Model):
    # Associando Veterinário ao Usuário
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='veterinarios')
    registro_crmv = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    
    # Associando Veterinário à Veterinária
    veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE, related_name='veterinarios')

    def __str__(self):
        return self.nome


class Prontuario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_atualizacao = models.DateTimeField(auto_now=True)
    observacoes = models.TextField()

    def adicionar_observacao(self, observacao: str):
        self.observacoes += f"\n{observacao}"
        self.save()  # É importante salvar a mudança no banco de dados

    def __str__(self):
        return f"Prontuário de {self.animal}"


class RegistroSaude(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return f"Registro de Saúde em {self.data_registro} para {self.prontuario.animal}"


class Vacina(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nome_vacina = models.CharField(max_length=100)
    data_vacinacao = models.DateField()
    dose = models.CharField(max_length=100)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_vacina} para {self.animal}"


class Exame(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=100)
    data_exame = models.DateField()
    resultado = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exame {self.tipo_exame} de {self.animal}"


class Alergia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_diagnostico = models.DateField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alergia de {self.animal} - {self.descricao}"


class Cirurgia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tipo_cirurgia = models.CharField(max_length=100)
    data_cirurgia = models.DateField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    descricao = models.TextField()
    resultado = models.TextField()

    def __str__(self):
        return f"{self.tipo_cirurgia} em {self.animal}"


class Documento(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=100)
    data_emissao = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return f"{self.tipo_documento} para {self.animal}"


class AtestadoSaude(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_emissao = models.DateField()
    condicao_saude = models.TextField()
    observacoes = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atestado de Saúde para {self.animal} - {self.data_emissao}"


class CarteiraVacinacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_emissao = models.DateField()
    vacinas = models.TextField()  # Pode ser uma lista de vacinas em formato de string
    observacoes = models.TextField()

    def __str__(self):
        return f"Carteira de Vacinação de {self.animal}"


class FichaClinica(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Dono, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    historico = models.TextField()
    anamnese = models.TextField()
    queixas_principais = models.TextField()
    queixas_secundarias = models.TextField()
    exame_fisico = models.TextField()
    suspeita_clinica = models.TextField()
    diagnostico_diferencial = models.TextField()
    exames_complementares = models.TextField()
    tratamento_prescrito = models.TextField()
    evolucao = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ficha Clínica de {self.animal} - {self.data_consulta}"


class Receituario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Dono, on_delete=models.CASCADE)
    data_emissao = models.DateField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    descricao_tratamento = models.TextField()
    quantidade_prescrita = models.CharField(max_length=100)  # Exemplos: '10 ml'
    via_administracao = models.CharField(max_length=100)
    observacoes = models.TextField()

    def __str__(self):
        return f"Receituário de {self.animal} - {self.data_emissao}"


class TermoConsentimento(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Dono, on_delete=models.CASCADE)
    data_emissao = models.DateField()
    observacoes = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Termo de Consentimento para {self.animal} - {self.data_emissao}"


class AtestadoObito(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Dono, on_delete=models.CASCADE)
    data_obito = models.DateField()
    hora_obito = models.TimeField()
    provavel_causa_mortis = models.TextField()
    idade = models.IntegerField()  # Idade em anos
    orientacao_destinacao_corpo = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atestado de Óbito de {self.animal}"


class Procedimento(models.Model):
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_estimativa = models.CharField(max_length=100)  # Pode ser um texto como '30 min'
    necessidade_anestesia = models.BooleanField()

    def __str__(self):
        return f"Procedimento: {self.descricao}"
