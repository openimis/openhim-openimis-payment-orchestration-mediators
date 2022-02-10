from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Patient


@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('id','firstname','lastname')