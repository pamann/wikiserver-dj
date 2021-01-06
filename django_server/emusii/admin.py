from django.contrib import admin
from .models import node, emoji


class emusiiAdmin(admin.ModelAdmin):
    list_display= ("title", "emoji")

admin.site.register(node)
admin.site.register(emoji)
