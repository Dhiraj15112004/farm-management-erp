from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('storekeeper', 'Storekeeper'),
        ('accountant', 'Accountant'),
        ('sales', 'Sales'),
        ('field_staff', 'Field Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='field_staff')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username