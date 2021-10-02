from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField('NAME', max_length=50, blank=True)
    phonenum = models.CharField('PHONE', max_length=50, blank=False)

    def __str__(self):
        return self.name
