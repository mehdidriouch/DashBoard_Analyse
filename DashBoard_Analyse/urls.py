from django.contrib import admin
from django.urls import path, include

from Dash import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dash.urls'))
]
