from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


    class Meta:
        app_label = 'myaplicacion'  # Reemplaza 'myaplicacion' con el nombre real de tu aplicación






