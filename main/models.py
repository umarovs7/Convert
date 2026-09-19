from django.db import models

# Create your models here.



class Distination(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Convert_blank(models.Model):
    name = models.CharField(max_length=255)
    date_day = models.DateField()
    date_time = models.TimeField()
    distination = models.ForeignKey(Distination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name