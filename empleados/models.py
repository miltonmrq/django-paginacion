from django.db import models

class Empleado(models.Model):
    titulo = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.titulo

