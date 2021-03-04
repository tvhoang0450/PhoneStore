from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.

class Trademark(models.Model):
    name = models.CharField(blank=False, max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(blank=False, max_length=100, validators=[MinLengthValidator(7)])
    trademark = models.ForeignKey(Trademark, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', default='images.jpg')
    price = models.DecimalField(max_digits=20, decimal_places=4, validators=[MinValueValidator(10000)])
    time_publish = models.DateTimeField(default=timezone.now)
    time_update = models.DateTimeField(blank=True, auto_now=True)
    description = models.TextField(blank=False, max_length=1000)

    def __str__(self):
        return self.name
