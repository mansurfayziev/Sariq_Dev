from django.shortcuts import render,redirect
from .models import Article
def home(request):
    a=Article.objects.order_by('-id')
    return render(request,'home.html',{'articles':a})


def addpost(request):
    if request.POST:
        a=Article.objects
        a.create(title=request.POST['name'],text=request.POST['text'])
        return redirect('home')
    return render(request,'addpost.html')

