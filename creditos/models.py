from django.db import models

class Creditos(models.Model):
    usuario = models.ForeignKey('users.User', on_delete=models.CASCADE)
    total_credito = models.IntegerField()
    monto_inicial = models.IntegerField()
    fecha_credito = models.DateField()

    def __str__(self):
        return f"Credito {self.id}"
