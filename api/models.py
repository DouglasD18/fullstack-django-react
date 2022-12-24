from django.db import models


class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.role} - {self.nome}"


class Car(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self) -> str:
        return f"{self.marca} {self.nome} {self.modelo}"
