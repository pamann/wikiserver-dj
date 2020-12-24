from django.contrib import admin
from .models import emusii


class emusiiAdmin(admin.ModelAdmin):
    list_display= ("title", "emoji")

# Register your models here.
admin.site.register(emusii, emusiiAdmin)
