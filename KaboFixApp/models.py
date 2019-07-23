from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class KaboRequest(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField()
    likes = models.ManyToManyField(User)
    status = models.BooleanField(default=False )
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='KaboProblem')
    def __str__(self):
        return "{} ({})".format(self.name, self.author.username)