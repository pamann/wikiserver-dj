from django.contrib import admin
from .models import emusii


class emusiiAdmin(admin.ModelAdmin):  # add this
    title = "title"  # add this


# Register your models here.
admin.site.register(emusii, emusiiAdmin)  # add this
