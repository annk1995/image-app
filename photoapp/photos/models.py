from turtle import title
from django.db import models
from django.forms import SlugField

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=20,)
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)