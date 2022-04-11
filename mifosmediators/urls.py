"""
django_openhim_mediators URL Configuration for MIFOS endpoints
"""
from django.contrib import admin
from django.urls import path

from . register_mediators import (getClient,getGroup,getOrganization,getInvoice,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fineract-provider/api/v1/clients',getClient),
    path('fineract-provider/api/v1/groups',getGroup),  
    path('fineract-provider/api/v1/organizations',getOrganization),      
    path('fineract-provider/api/v1/invoices',getInvoice),
]