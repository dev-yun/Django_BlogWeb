from django.contrib import admin

# Register your models here.
from phone.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phonenum')