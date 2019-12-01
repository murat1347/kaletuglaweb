from django.shortcuts import render,HttpResponse
from .models import Urunler,Blog
# Create your views here.
def index(request):
    return render(request,"index.html")

def hakkimizda(request):
    return render(request,"hakkimizda.html")

def iletisim(request):
    return render(request,"iletisim.html")

def urunler(request,id=1):
    urunler = Urunler.objects.all()
    return render(request,"urunler.html",{'urunler':urunler})

def urundetay(request,id):
    return render(request,"urundetay.html",{'urun':Urunler.objects.get(pk=id)})

def blog(request):
    yazilar=Blog.objects.all()
    return render(request,"blog.html",{'yazilar':yazilar})

def yazilar(request,id):
    return render(request,"yazilar.html",{'yazi':Blog.objects.get(pk=id)})