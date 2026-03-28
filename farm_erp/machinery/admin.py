from django.contrib import admin
from .models import Equipment, UsageLog, Maintenance

admin.site.register(Equipment)
admin.site.register(UsageLog)
admin.site.register(Maintenance)