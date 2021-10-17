from django.db import models
from django.db.models.base import Model

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    desc = models.TextField(max_length=150)
    qnt = models.IntegerField()
    # total = price*qnt

    def __str__(self):
        return self.name