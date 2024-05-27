from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .comment_and_post_form import PostForm, CommentForm



def index(request):
    post_objects = Post.objects.all()
    return render(request, 'index.html', {'title':'Post List', 'post':post_objects})    

def postdetail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'title':post.title, 'post':post})

def postform(request):
    if request.method == "POST":
        formpost = PostForm(request.POST)
        if formpost.is_valid():
            formpost.save()
            return redirect('index')
    else:
        formpost = PostForm()
    return render(request, 'postform.html', {'title':'Form Posting', 'form':formpost})