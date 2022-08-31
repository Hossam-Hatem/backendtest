from django.shortcuts import render
from .models import Post
from .forms import Postform


# Create your views here.


def post_list(request):
    objects=Post.objects.all()
    return render(request,'posts.html',{'posts':objects})

def singel_post(request,id):
    single=Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':single})

def new_post(request):
    if request.method=='POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=Postform()
    return render(request,'new.html',{'form':form})


def edit_post(request,id):
    single=Post.objects.get(id=id)
    if request.method=='POST':
        form=Postform(request.POST,request.FILES,instance=single)
        if form.is_valid():
            form.save()
    else:
        form=Postform(instance=single)

    return render(request,'edit.html',{'form':form})
