from django.db import models

# Create your models here.

class info(models.Model):
    f_name = models.CharField(max_length=20,unique=True)
    l_name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.f_name
