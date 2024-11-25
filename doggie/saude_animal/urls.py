from django.urls import path
from .views import *

urlpatterns = [
    
    # URLs para Usuario
    path('usuarios/', UsuarioView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuarioView.as_view(), name='usuario-detail'),

    # URLs para Endereco
    path('enderecos/', EnderecoView.as_view(), name='enderecos-list'),  # Listar e criar endereços
    path('enderecos/<int:pk>/', EnderecoView.as_view(), name='endereco-detail'),  # Detalhar, atualizar e deletar endereços

    # URLs para Dono
    path('donos/', DonoView.as_view(), name='donos-list'),
    path('donos/<int:pk>/', DonoView.as_view(), name='dono-detail'),

    # URLs para Animal
    path('animais/', AnimalView.as_view(), name='animais-list'),
    path('animais/<int:pk>/', AnimalView.as_view(), name='animal-detail'),

    # URLs para Especialidade
    path('especialidades/', EspecialidadeView.as_view(), name='especialidades-list'),
    path('especialidades/<int:pk>/', EspecialidadeView.as_view(), name='especialidade-detail'),

    # URLs para Veterinaria
    path('veterinarias/', VeterinariaView.as_view(), name='veterinarias-list'),
    path('veterinarias/<int:pk>/', VeterinariaView.as_view(), name='veterinaria-detail'),

    # URLs para Veterinario
    path('veterinarios/', VeterinarioView.as_view(), name='veterinarios-list'),
    path('veterinarios/<int:pk>/', VeterinarioView.as_view(), name='veterinario-detail'),

    # URLs para Prontuario
    path('prontuarios/', ProntuarioView.as_view(), name='prontuarios-list'),
    path('prontuarios/<int:pk>/', ProntuarioView.as_view(), name='prontuario-detail'),

    # URLs para Registro de Saúde
    path('registros-saude/', RegistroSaudeView.as_view(), name='registros-saude-list'),
    path('registros-saude/<int:pk>/', RegistroSaudeView.as_view(), name='registro-saude-detail'),

    # URLs para Vacina
    path('vacinas/', VacinaView.as_view(), name='vacinas-list'),
    path('vacinas/<int:pk>/', VacinaView.as_view(), name='vacina-detail'),

    # URLs para Exame
    path('exames/', ExameView.as_view(), name='exames-list'),
    path('exames/<int:pk>/', ExameView.as_view(), name='exame-detail'),

    # URLs para Alergia
    path('alergias/', AlergiaView.as_view(), name='alergias-list'),
    path('alergias/<int:pk>/', AlergiaView.as_view(), name='alergia-detail'),

    # URLs para Cirurgia
    path('cirurgias/', CirurgiaView.as_view(), name='cirurgias-list'),
    path('cirurgias/<int:pk>/', CirurgiaView.as_view(), name='cirurgia-detail'),

    # URLs para Documento
    path('documentos/', DocumentoView.as_view(), name='documentos-list'),
    path('documentos/<int:pk>/', DocumentoView.as_view(), name='documento-detail'),

    # URLs para Atestado de Saúde
    path('atestados-saude/', AtestadoSaudeView.as_view(), name='atestados-saude-list'),
    path('atestados-saude/<int:pk>/', AtestadoSaudeView.as_view(), name='atestado-saude-detail'),

    # URLs para Carteira de Vacinação
    path('carteiras-vacinacao/', CarteiraVacinacaoView.as_view(), name='carteiras-vacinacao-list'),
    path('carteiras-vacinacao/<int:pk>/', CarteiraVacinacaoView.as_view(), name='carteira-vacinacao-detail'),

    # URLs para Ficha Clínica
    path('fichas-clinicas/', FichaClinicaView.as_view(), name='fichas-clinicas-list'),
    path('fichas-clinicas/<int:pk>/', FichaClinicaView.as_view(), name='ficha-clinica-detail'),

    # URLs para Receituário
    path('receituarios/', ReceituarioView.as_view(), name='receituarios-list'),
    path('receituarios/<int:pk>/', ReceituarioView.as_view(), name='receituario-detail'),

    # URLs para Termo de Consentimento
    path('termos-consentimento/', TermoConsentimentoView.as_view(), name='termos-consentimento-list'),
    path('termos-consentimento/<int:pk>/', TermoConsentimentoView.as_view(), name='termo-consentimento-detail'),

    # URLs para Atestado de Óbito
    path('atestados-obito/', AtestadoObitoView.as_view(), name='atestados-obito-list'),
    path('atestados-obito/<int:pk>/', AtestadoObitoView.as_view(), name='atestado-obito-detail'),

    # URLs para Procedimento
    path('procedimentos/', ProcedimentoView.as_view(), name='procedimentos-list'),
    path('procedimentos/<int:pk>/', ProcedimentoView.as_view(), name='procedimento-detail'),
]