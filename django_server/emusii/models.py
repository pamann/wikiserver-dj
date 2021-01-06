from django.db import models

class emoji(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def _str_(self):
        return self.title

class node(models.Model):
    song_id = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    _emoji = models.ForeignKey(emoji, on_delete=models.CASCADE)
    channel = models.CharField(max_length=120)
    nav_options = models.ManyToManyField("self", related_name="nav")

    def _str_(self):
        return self.title

class activesubgraph(models.Model):
    active = models.ForeignKey(node, on_delete=models.CASCADE, related_name="active")
    nodes = models.ManyToManyField(node)

    def _str_(self):
        return self.active

class graph(models.Model):
    graph = models.ForeignKey(node, on_delete=models.CASCADE)
    def _str_(self):
        return self.graph