from django.db import models

class Markssheet(models.Model):
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Biology=models.IntegerField()
    Chemistry=models.IntegerField()
    English=models.IntegerField()
    Total=models.IntegerField()
    Percentage=models.FloatField()

# Create your models here.
