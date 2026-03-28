from django.db import models
from master_setup.models import Field, Crop


class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='Planned')

    def __str__(self):
        return self.name


class FieldCropPlan(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    sowing_date = models.DateField()
    expected_harvest_date = models.DateField()
    expected_yield = models.FloatField()
    expected_budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.field.name} - {self.crop.name} ({self.season.name})"