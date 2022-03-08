from django.db import models

# Create your models here.

class cashFlow(models.Model):
    tanggal = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=1000)
    kuantitas = models.CharField(max_length=100)
    nominal	= models.CharField(max_length=100)  