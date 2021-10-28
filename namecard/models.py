from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Namecard_TBL(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    tel = models.CharField('MOBILE', max_length=50, blank=False)
    company = models.CharField('COMPANY', max_length=50, blank=True)
    email = models.EmailField('EMAIL', max_length=50, blank=True)
    group = models.CharField('Group', max_length=50, blank=True)
    creat_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('namecard:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ('group', 'name',)


