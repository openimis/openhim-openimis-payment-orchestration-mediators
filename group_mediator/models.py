from django.db import models
  
class Group(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True,
         verbose_name ='Group ID')
    externalID = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    officeName = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'clients_group'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('id','name')
        
    def __str__(self):
        return self.name
