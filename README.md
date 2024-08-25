# Worshop_Fabrica_2024.2_MatheusRyan 🚀
Fabrica de software 2024.2


## Features ✨

- CRUD Completo: Implementação de operações de Create, Read, Update e Delete para as entidades Estado e Cidade.
- Consumo de API Externa: A aplicação consome uma API para verificar e obter informações de fuso horário (UTC) com base no país informado na entidade Estado.
- Autenticação JWT (opcional): Integração opcional de autenticação via JWT (JSON Web Token) para proteger e assegurar as operações realizadas na API.
- Integração com Banco de Dados MySQL: Persistência de dados utilizando o banco MySQL, garantindo armazenamento confiável das informações das entidades.

##

##Como Funciona 🔩
Integração com OpenLibrary: Quando um novo livro é criado, o sistema faz uma requisição à API OpenLibrary para obter informações adicionais sobre o livro, como o título e o autor. Se o autor não existir na base de dados, ele é criado automaticamente.

##

# Livraria 📘

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework. A API é projetada para gerenciar informações sobre livros e autores e utiliza a API externa OpenLibrary para obter dados adicionais sobre os livros.

## Funcionalidades 

- **Gerenciamento de Livros**: Cria, lê, atualiza e exclui informações sobre livros.
- **Gerenciamento de Autores**: Cria, lê, atualiza e exclui informações sobre autores.
- **Integração com OpenLibrary**: Busca informações dos livros através da API OpenLibrary.

- ## Estrutura do Projeto 🔧

O projeto é dividido em dois aplicativos Django:

- **livros**: Gerencia informações sobre livros.
- **autores**: Gerencia informações sobre autores.

- ### Instalação e Configuração

1. **Clonar o Repositório**

   Clone o repositório para o seu ambiente local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <DIRETORIO_DO_PROJETO>

   Criar e Ativar um Ambiente Virtual

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Unix
   venv\Scripts\activate  # Para Windows

3 **Instalar Dependências**

Instale as dependências do projeto localizadas no requirements.txt

   ```bash
   pip install -r requirements.txt
   ```



4. **Configurar o Banco de Dados**

Crie e aplique as migrações para configurar o banco de dados:

   ```bash
   Copiar código
   python manage.py makemigrations
   python manage.py migrate
   Executar o Servidor

   Inicie o servidor de desenvolvimento:

   bash
   Copiar código
   python manage.py runserver
   ```


##Como utilizar 📝
Após todos os passos de configurações serem realizados, você ira receber um link para acessar a API, similar ou igual a este: http://127.0.0.1:8000/

**Endpoints da API**

##Livros 📚

Listar Livros: GET /api/livros/
Retorna uma lista de todos os livros.

Criar Livro: POST /api/livros/
Cria um novo livro. Requer o campo isbn para buscar informações na API OpenLibrary.

Detalhes do Livro: GET /api/livros/{id}/
Retorna os detalhes de um livro específico.

Atualizar Livro: PUT /api/livros/{id}/
Atualiza as informações de um livro específico.

Excluir Livro: DELETE /api/livros/{id}/
Exclui um livro específico.

## Autores 👩‍🎓
Listar Autores: GET /api/autores/
Retorna uma lista de todos os autores.

Criar Autor: POST /api/autores/
Cria um novo autor.

Detalhes do Autor: GET /api/autores/{id}/
Retorna os detalhes de um autor específico.

Atualizar Autor: PUT /api/autores/{id}/
Atualiza as informações de um autor específico.

Excluir Autor: DELETE /api/autores/{id}/
Exclui um autor específico.

##

## Desenvolvimento
Criar um Novo Aplicativo: Utilize python manage.py startapp <nome_do_app> para criar novos aplicativos no projeto.
Adicionar Novos Modelos: Defina novos modelos no arquivo models.py do aplicativo correspondente.
Adicionar Novos Endpoints: Crie novos viewsets e serializers para adicionar endpoints adicionais.


