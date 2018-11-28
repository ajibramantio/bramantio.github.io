from django.db import models

# Create your models here.
class Subscriber(models.Model):
    nama = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True, primary_key=True)
    password = models.CharField(max_length=20)

    def as_dict(self):
        return{
			"email": self.email,
			"nama": self.nama,
			"password": self.password,
		}
        
    def __str__(self):
        return "{}".format(self.email)
