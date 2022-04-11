from django.db import models

# Create your models here.
class Organization(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True,
         verbose_name ='Corporate ID')
    externalID = models.CharField(max_length=45)
    fullname = models.CharField(max_length=255, 
        blank=True, null=True,)

    class Meta:
        managed = True
        db_table = 'client_organization'
        verbose_name = 'Organization Info'
        verbose_name_plural = 'Organization Details'
        ordering = ('id','fullname')
        