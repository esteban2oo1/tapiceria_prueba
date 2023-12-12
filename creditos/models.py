from django.db import models

class Creditos(models.Model):
    usuario = models.CharField(max_length=150)    
    total_credito = models.IntegerField()
    monto_inicial = models.IntegerField()
    fecha_credito = models.DateField()

    def __str__(self):
        return f"Credito {self.usuario}"
