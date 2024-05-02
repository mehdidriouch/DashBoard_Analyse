import os
import uuid  # Pour générer des UUIDs

import pandas as pd
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from Dash.models import FichierTelecharge


# Create Page Load File.
def Traitement_Fichier(request):
    pass

# Create Page Load File.
def LoadFilePage(request):
    if request.method == 'POST':
        # Obtenir tous les fichiers associés au nom de champ 'multiexcelfile' on utilisent getlist
        files = request.FILES.getlist('multiexcelfile')
        if files:
            for file in files:
                # Vérifiez si chaque fichier est un fichier Excel
                if not file.name.lower().endswith(('.xlsx', '.xls')):
                    messages.error(request, "Uniquement les fichiers Excel doivent être utilisés...")
                    return redirect('/')  # Rediriger vers la même page si erreur existe
                else:
                    #? Si tous les fichiers sont valides, On vas essai d'affecter un uuid a chaque fichier importé pour identifier de manière unique les fichiers téléchargés. ce qui peut également améliorer la sécurité et la gestion des fichiers.
                    # Générer un UUID et renommer le fichier avec cet UUID
                    unique_id = uuid.uuid4()  # UUID unique
                    extension = os.path.splitext(file.name)[1]  # Conserver l'extension
                    unique_filename = f"{unique_id}{extension}"  # Nom unique

                    # Chemin de stockage basé sur le nom unique
                    file_path = os.path.join('fichiers', unique_filename)

                    # # Créer une instance du modèle avec le chemin du fichier
                    # new_file_instance = FichierTelecharge.objects.create(fichier=file_path)

                    # # Enregistrer le fichier dans le stockage par défaut avec le nouveau nom
                    # new_file_instance.fichier.save(unique_filename, ContentFile(file.read()))

                    # # Sauvegarder l'instance dans la base de données
                    # new_file_instance.save()

                    print("Fichier reçu et enregistré :", file_path)

            return redirect('DashBoard_Page')
        else:
            messages.warning(request, "Aucun fichier n’a été téléchargé")
        
    return render(request, 'loadFilePage.html')

# Create Page DashBoard.
def DashBoard_Page(request):
    return render(request, 'dashBoard_Page.html')

