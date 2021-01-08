from django.db import models

class emoji(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def _str_(self):
        return self.title

class node(models.Model):
    song_id = models.CharField(max_length=120, primary_key=True, unique=True)
    title = models.CharField(max_length=120)
    _emoji = models.ForeignKey(emoji, on_delete=models.CASCADE)
    channel = models.CharField(max_length=120)
    N = models.ForeignKey("self", on_delete=models.CASCADE, related_name="N_nav", null=True, blank=True)
    E = models.ForeignKey("self", on_delete=models.CASCADE, related_name="E_nav", null=True, blank=True)
    S = models.ForeignKey("self", on_delete=models.CASCADE, related_name="S_nav", null=True, blank=True)
    W = models.ForeignKey("self", on_delete=models.CASCADE, related_name="W_nav", null=True, blank=True)

    def _str_(self):
        return self.title
