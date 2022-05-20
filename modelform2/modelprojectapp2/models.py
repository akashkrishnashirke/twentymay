from django.db import models

# Create your models here.
class mobiles_fiturs_model(models.Model):
    name=models.CharField(max_length=20)
    idd=models.IntegerField(primary_key=True)
    ram=models.CharField(max_length=20)
    rom=models.CharField(max_length=20)
    storage=models.CharField(max_length=20)
    camera=models.CharField(max_length=20)
    android_version=models.CharField(max_length=20)
    warranty=models.CharField(max_length=20)




