from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True,
         verbose_name ='Client ID')
    externalID = models.CharField(max_length=45)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255, 
        blank=True, null=True,)

    class Meta:
        managed = True
        db_table = 'client_person'
        verbose_name = 'Client Info'
        verbose_name_plural = 'Client Details'
        ordering = ('id','fullname')
        