from django.contrib import admin
from .models import node, emoji, activesubgraph, graph


class emusiiAdmin(admin.ModelAdmin):
    list_display= ("title", "emoji")

admin.site.register(node)
admin.site.register(activesubgraph)
admin.site.register(graph)
admin.site.register(emoji)

