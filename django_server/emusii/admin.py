from django.contrib import admin
from .models import emusii, graph, emoji


# class emusiiAdmin(admin.ModelAdmin):
#     list_display= ("title", "emoji")

admin.site.register(emusii)
admin.site.register(graph)
admin.site.register(emoji)

