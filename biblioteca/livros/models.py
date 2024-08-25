from django.db import models
from autores.models import Autor

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.titulo
