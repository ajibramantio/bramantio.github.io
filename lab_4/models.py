from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Sched(models.Model):
    nama = models.CharField(max_length=80)
    tanggal = models.DateField()
    jam = models.TimeField()
    tempat = models.CharField(max_length=80)
    kategori = models.CharField(max_length=80)
