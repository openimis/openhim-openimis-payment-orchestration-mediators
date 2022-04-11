from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Group


@admin.register(Group)
class GroupAdmin(ImportExportModelAdmin):
    list_display = ('id','externalID','name','officeName',)