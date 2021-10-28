from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    univ = models.CharField(max_length=20, blank=False, null=False)
    tel = models.CharField(max_length=15, blank=True, null=True)
    group = models.CharField(max_length=20, blank=False, null=False)
    studentnum = models.CharField(max_length=9, blank=False, null=False)
    modify_dt = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.id})
