from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.email}"

