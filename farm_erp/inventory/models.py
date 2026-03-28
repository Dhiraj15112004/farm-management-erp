from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_stock = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class StockIn(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f"Stock In - {self.item.name}"


class StockOut(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    issued_to = models.CharField(max_length=100)

    def __str__(self):
        return f"Stock Out - {self.item.name}"