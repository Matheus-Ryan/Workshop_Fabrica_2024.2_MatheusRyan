from rest_framework import serializers
from .models import Livro
from autores.serializers import AutorSerializer

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'isbn']
