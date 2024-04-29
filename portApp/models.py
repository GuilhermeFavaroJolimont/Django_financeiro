from django.db import models

# Create your models here.

class Devedores(models.Model):
    cliente = models.CharField(max_length=255)
    divida = models.FloatField()
    descricao = models.TextField()
    pagou = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True)