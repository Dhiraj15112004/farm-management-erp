from django.db import models


class Harvest(models.Model):
    crop = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.crop


class Sale(models.Model):
    crop = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.crop