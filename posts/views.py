from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Product
from .models import Review

# Create your views here.

def new(request):
    form = PostForm()
    return render(request, 'posts/new.html', {'form':form})
    

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user = request.user)
        return redirect('posts:main')


def main(request):
    posts = Product.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def show(request, id):
    post = Product.objects.get(pk=id)
    post.save()
    return render(request, 'posts/show.html', {'post': post})


def update(request,id):
    post = get_object_or_404(Product,pk=id)
    if request.method == "POST":
        post.item = request.POST['item']
        post.explanation = request.POST['explanation']
        post.price = request.POST['price']
        post.stock = request.POST['stock']
        post.image = request.FILES.get('image') 
        post.save()
        return redirect('posts:show',post.id)
    return render(request, 'posts/update.html',{"post":post})


def delete(request,id):
    post = get_object_or_404(Product,pk=id)
    post.delete()
    return redirect("posts:main")

