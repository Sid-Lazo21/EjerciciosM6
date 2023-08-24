from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='tu@email.com')
    password = models.CharField(max_length=100, default=1)

    def __str__(self):
        return self.nombre
    class Meta:
        app_label = 'myaplicacion'  # Reemplaza 'myaplicacion' con el nombre real de tu aplicación















