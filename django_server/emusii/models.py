from django.db import models

class emoji(models.Model):
    title = models.CharField(max_length=50)
    word = models.CharField(max_length=50)
        def _str_(self):
            return self.title

class emusii(models.Model):
    title = models.CharField(max_length=120)
    emoji = models.ForeignKey(emoji, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

class graph(models.Model):
    active = models.ForeignKey(emusii, on_delete=models.CASCADE, related_name="active")
    nodes = models.ManyToManyField(emusii, related_name="nodes")
    nav_options = models.ManyToManyField(emoji)

