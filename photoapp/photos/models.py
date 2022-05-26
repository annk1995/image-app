
from django.db import models


# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=20,)
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)