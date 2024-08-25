from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer
import requests

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def perform_create(self, serializer):
        isbn = serializer.validated_data['isbn']
        response = requests.get(f'https://openlibrary.org/isbn/{isbn}.json')
        if response.status_code == 200:
            data = response.json()
            titulo = data.get('title', 'Título desconhecido')
            autor_nome = data.get('authors', [{'name': 'Autor desconhecido'}])[0]['name']
            
            # If para verificalçao de existencia do autor.
            from autores.models import Autor
            autor, created = Autor.objects.get_or_create(nome=autor_nome)
            
            serializer.save(titulo=titulo, autor=autor)
        else:
            serializer.save()
