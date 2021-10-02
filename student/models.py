from django.db import models

# Create your models here.

class Student(models.Model):
    univ = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=10, blank=False, null=False)
    tel = models.CharField(max_length=15, blank=True, null=True)
    group = models.CharField(max_length=20, blank=False, null=False)
    studentnum = models.CharField(max_length=9, blank=False, null=False)
    modify_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name