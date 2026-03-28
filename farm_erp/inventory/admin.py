from django.contrib import admin
from .models import InventoryItem, StockIn, StockOut

admin.site.register(InventoryItem)
admin.site.register(StockIn)
admin.site.register(StockOut)