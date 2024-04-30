from django.db import models

# Create your models here.
class Exemple(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    age = models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.name)