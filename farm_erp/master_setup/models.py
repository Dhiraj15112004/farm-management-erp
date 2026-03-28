from django.db import models


class FarmProfile(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_area = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=100)
    area = models.FloatField()
    soil_type = models.CharField(max_length=50)
    irrigation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    purchase_date = models.DateField()
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.name