# 💻 API Doggie Heart - Desenvolvimento Web II

Este repositório contém o projeto de uma API REST desenvolvida durante a disciplina de **Desenvolvimento Web II** no **IFPR - Campus Cascavel**.

O projeto, chamado **doggie heart**, utiliza o framework **Django** para criar um sistema de saúde animal, com foco em rotas de API para gerenciamento de dados.

---

## ⚙️ Tecnologias e Conceitos
- **Python** → linguagem de programação
- **Django** → framework web back-end
- **Django REST Framework (DRF)** → para a criação da API REST
- **SQLite** → banco de dados padrão para desenvolvimento
- **API REST** → comunicação entre cliente e servidor
- **ORM** → Mapeamento Objeto-Relacional
- **MVT (Model-View-Template)** → padrão de design do Django

---

## 📌 Visão Geral do Projeto
A API `doggie` foi criada para simular um sistema de gerenciamento de saúde animal. O projeto inclui um aplicativo principal (`doggie`) e um aplicativo secundário (`saude_animal`), onde estão os modelos de dados, serializadores e views da API. O projeto demonstra a criação de endpoints, serialização de dados e manipulação de banco de dados.

---

## 📁 Estrutura do Repositório
```bash
doggie/
├── doggie/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
├── saude_animal/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── DER.pdf
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── ...

```

> A estrutura reflete um projeto Django, com um aplicativo principal e um aplicativo dedicado ao domínio da saúde animal.

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
      git clone https://github.com/ifpr-fushisuno/ifpr-web-2.git
      cd doggie
   ```
2. Crie e ative um ambiente virtual:
   ```bash
      python -m venv venv
      source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
      pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
      python manage.py makemigrations
      python manage.py migrate
   ```

5. Inicie o servidor local:
   ```bash
      python manage.py runserver
   ```
A API estará disponível em `http://127.0.0.1:8000/`.

---

## 🎯 Objetivos do Repositório
- Consolidar conhecimentos em desenvolvimento web back-end.
- Aprender a utilizar o framework Django para criar APIs REST.
- Entender o fluxo de dados em uma aplicação Django.
- Servir como material de referência para projetos futuros.

---

## 🔗 Links úteis
- [Documentação do Django](https://docs.djangoproject.com/en/)
- [Documentação do Django REST Framework](https://www.django-rest-framework.org/)

---

✍️ Mantido por [Kainã (fushisuno)](https://github.com/fushisuno)
