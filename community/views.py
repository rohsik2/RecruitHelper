from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from datetime import date


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'community/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = comment_list(post)
    return render(request, 'community/post_detail.html', {'post': post, 'comments':comments})


def calendar(request):
    return render(request, 'community/calendar.html')


def post_new(request):
    if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.published_date = timezone.now()
           post.save()
           return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'community/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_list)
    else:
        form = PostForm(instance=post)
    return render(request, 'community/post_edit.html', {'form': form})


def comment_list(post):
    comments = Comment.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return comments

def left_day(request):
    d_start = date(2019, 9, 2)
    d_fin = date(2021, 6, 16)
    d_delta = d_start-d_fin
    return render(request, 'community/left_day.html', {'leftday': d_delta})

