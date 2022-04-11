from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin):
    list_display = ('id','externalID','fullname')