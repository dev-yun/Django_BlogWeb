from django.contrib import admin

# Register your models here.
from namecard.models import Namecard_TBL


@admin.register(Namecard_TBL)
class NamecardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'tel', 'company', 'email')