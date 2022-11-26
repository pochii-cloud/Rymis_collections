from django.db import models


# Create your models here.
class County(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(County, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    fee = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name
