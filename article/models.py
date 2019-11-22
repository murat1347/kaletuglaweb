from django.db import models

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField()
class Urunler(models.Model):
    id = models.AutoField(primary_key=True)
    urunismi = models.CharField(max_length=50)
    urun_content = models.CharField(max_length=400)
    