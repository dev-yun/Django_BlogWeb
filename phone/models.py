from django.db import models

# Create your models here.
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField('NAME', max_length=50, blank=True)
    phonenum = models.CharField('PHONE', max_length=50, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone:number', kwargs={'pk': self.id})
