from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.UUIDField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'mediator_patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        
    def __str__(self):
        return self.lastname