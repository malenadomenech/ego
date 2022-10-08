from django.db import models

# Create your models here
class vehiculo(models.Model):
    name=models.CharField(max_length=50)
    year=models.PositiveIntegerField()
    price=models.PositiveBigIntegerField()

