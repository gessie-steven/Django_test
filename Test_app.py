Débuter un projet Django 

# Étape 1: Création du projet Django
django-admin startproject nom_projet // python -m django startproject Test_app

cd Test_app

# Étape 2: Création d'une application
django-admin startapp app

# Étape 3: Modifier settings.py pour inclure l'application
# nom_projet/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Ajout de l'application principale
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app/templates'],  # Définition du dossier des templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'app/static']

# Étape 4: Configurer les URLs principales
# Test_app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Rediriger vers l'application principale
]

# Étape 5: Configurer les URLs de l'application
# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
]

# Étape 6: Créer la vue pour la page d'accueil
# app/views.py
from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')

# Étape 7: Créer un template pour la page d'accueil
# app/templates/accueil.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plateforme Grossistes Sénégal</title>
</head>
<body>
    <h1>Bienvenue sur la plateforme de Grossistes du Sénégal</h1>
</body>
</html>
