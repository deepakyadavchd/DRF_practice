from django.db import models


class Car(models.Model):
    brandname = models.CharField(max_length=200)
    modelname = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    milage = models.CharField(max_length=122)
    rentperday = models.IntegerField()

    def __str__(self):
        return self.brandname
