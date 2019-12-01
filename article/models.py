from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=90,verbose_name="Başlık")
    content=RichTextField()
    yazi_resmi=models.FileField(blank=True,null =True,verbose_name="Yazı Resmi")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Urunler(models.Model):
    id = models.AutoField(primary_key=True)
    urunismi = models.CharField(max_length=50,verbose_name="Urun ismi")
    urun_content = models.CharField(max_length=400,verbose_name="İçerik")
    urun_en=models.CharField(max_length=4,blank=True,null =True,verbose_name="En")
    urun_boy=models.CharField(max_length=4,blank=True,null =True,verbose_name="Boy")
    urun_yukseklik=models.CharField(max_length=4,blank=True,null =True,verbose_name="Yükseklik")
    urun_resmi= models.FileField(blank=True,null =True,verbose_name="Fotograf")
    urun_agirlik=models.CharField(max_length=4,blank=True,null =True,verbose_name="Ağırlık")
    def __str__(self):
        return self.urunismi