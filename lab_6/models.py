from django.db import models

# Create your models here.
class Statuy(models.Model):
    status = models.CharField(max_length=80)
    isi_status = models.CharField(max_length=80)