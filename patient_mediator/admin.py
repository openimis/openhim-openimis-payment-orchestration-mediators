from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Person


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','externalID','fullname',)