from django.contrib import admin

# Register your models here.
from AppCoder.models import Curso, Estudiante, Profesor

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
