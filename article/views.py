from django.shortcuts import render,HttpResponse
from .models import Urunler,Blog
from .models import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
def index(request):
    return render(request,"index.html")

def hakkimizda(request):
    return render(request,"hakkimizda.html")

def iletisim(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title=form.cleaned_data['title']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            contact_message="Gönderen : {0} \n  Email : {1} \n  Başlık : {2}\n Mesaj içeriği : {3}\n".format(name,email,title,message)
            
            try:
                send_mail(title,contact_message,settings.EMAIL_HOST_USER,['xfireware@gmail.com'],fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success')
    return render(request,"iletisim.html",{'form': form})

def success(request):
    
    return render(request,"success.html")
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


