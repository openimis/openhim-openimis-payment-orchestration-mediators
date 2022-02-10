"""
django_openhim_mediators URL Configuration for MIFOS endpoints
"""
from django.contrib import admin
from django.urls import path

from .register_mediators import getClient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fineract-provider/api/v1/clients', getClient),

]

