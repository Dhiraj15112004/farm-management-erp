from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UsageLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.IntegerField()
    fuel_used = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.equipment.name


class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.equipment.name