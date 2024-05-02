import uuid

from django.db import models


# Create your models here.
class FichierTelecharge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fichier = models.FileField()
    
    def __str__(self):
        return str(self.fichier.name)  # Afficher le nom du fichier comme représentation textuelle