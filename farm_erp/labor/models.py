from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    daily_wage = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.worker.name} - {self.date}"


class LaborTask(models.Model):
    task_name = models.CharField(max_length=100)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.task_name