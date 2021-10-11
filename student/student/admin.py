from django.contrib import admin

# Register your models here.
from student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'studentnum', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'tel', 'studentnum')